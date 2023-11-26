from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework import mixins 
from rest_framework import filters, generics, status, viewsets
# from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.response import Response
from rest_framework.throttling import (AnonRateThrottle, ScopedRateThrottle,
                                       UserRateThrottle)
from rest_framework.views import APIView

from movie_app.api.pagination import (MovieListCursorPagination,
                                          MovieListLimitOffsetPagination,
                                          MovieListPagination)
from movie_app.api.permissions import (IsAdminOrReadOnly,
                                           IsReviewUserOrReadOnly)
from movie_app.api.serializers import *
from movie_app.api.throttling import (ReviewCreateThrottle,
                                          ReviewListThrottle)
from movie_app.models import Review, StreamPlatform, Movie
from django.contrib.auth.models import User
from django.http import HttpResponse

class UserReview(generics.ListAPIView):
    # queryset = Review.objects.all() to customize the queryset
    serializer_class = ReviewSerializer
    # permission_classes = [IsAuthenticated]
    # throttle_classes = [ReviewListThrottle, AnonRateThrottle]
    
    # def get_queryset(self):
    #     username = self.kwargs['username']
    #     return Review.objects.filter(review_user__username=username)
    
    def get_queryset(self):
        username = self.request.query_params.get('username', None)
        return Review.objects.filter(review_user__username=username)

class ReviewList(generics.ListAPIView):
    # queryset = Review.objects.all() to customize the queryset
    serializer_class = ReviewSerializer
    # permission_classes = [IsAuthenticated]
    throttle_classes = [ReviewListThrottle, AnonRateThrottle]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['review_user__username', 'active']
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(movie=pk)
    
class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewUserOrReadOnly]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'review-detail'
    
class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [ReviewCreateThrottle]
    def create(self, request, *args, **kwargs):
        # Set the custom request variable
        self.request = request
        return super().create(request, *args, **kwargs)
    
    def get_queryset(self):
        return Review.objects.all()
    
    # this is overriding a GenericApiView method, which is called by CraeteApiview
    # https://www.django-rest-framework.org/api-guide/generic-views/#concrete-view-classes -> save and deletion hooks
    def perform_create(self, serializer): #override and customize the create method of createapiview
        pk = self.kwargs.get('pk')
        movie = Movie.objects.get(pk=pk)
        
        
        review_queryset = Review.objects.filter(review_user=self.request.user, movie=movie)
        if review_queryset.exists():
            raise ValidationError('You have already reviewed this movie!')
        
        if movie.number_rating == 0:
            movie.avg_rating = serializer.validated_data['rating']
        else:
            movie.avg_rating = (movie.avg_rating * movie.number_rating + serializer.validated_data['rating']) / (movie.number_rating + 1)
        
        movie.number_rating = movie.number_rating + 1
        movie.save()
        
        serializer.save(movie=movie, review_user=self.request.user) # saving the review for that particular movie


# class ReviewList(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class ReviewDetail(mixins.RetrieveModelMixin, GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

# to test search only
class MovieSearchView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    # Cursor pagination defaults to created time based ordering and ASKS to disable other ordering
    # filter_backends = [filters.OrderingFilter] 
    # ordering_fields = ['avg_rating']
    pagination_class = MovieListCursorPagination
    
    
class MovieListGetCreateView(APIView):
    permission_classes = [IsAdminOrReadOnly]
    def get(self, request):
        # Simulate a 401 response for demonstration purposes
        # return HttpResponse(status=401)
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MovieDetailView(APIView):
    permission_classes = [IsAdminOrReadOnly]
    
    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        movie = self.get_object(pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    
    def put(self, request, pk):
        movie = self.get_object(pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Modelviewset provides, list, post, individual item get, put, delete
#readonly viewset provides only list, and individual get method
class StreamPlatformViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows stream platforms to be viewed or edited.

    This viewset automatically provides `list`, `create`, `retrieve`,
    `update`, and `destroy` actions.

    * `list`: Returns a list of all stream platforms.
    * `create`: Creates a new stream platform.
    * `retrieve`: Retrieves a specific stream platform.
    * `update`: Updates a specific stream platform.
    * `destroy`: Deletes a specific stream platform.

    ## Additional Info:
    - Only admins can edit stream platforms.
    - ...

    """
    permission_classes = [IsAdminOrReadOnly]
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer
    
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
# class StreamPlatformViewSet(viewsets.ViewSet):
    
#     def list(self, request):
#         queryset = StreamPlatform.objects.all()
#         serializer = StreamPlatformSerializer(queryset, many=True, context={'request': request})
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = StreamPlatform.objects.all()
#         watchlist = get_object_or_404(queryset, pk=pk)
#         serializer = StreamPlatformSerializer(watchlist, context={'request': request})
#         return Response(serializer.data)
    
#     def create(self, request):
#         serializer = StreamPlatformSerializer(data=request.data, context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class StreamPlatformView(APIView):
#     def get(self, request):
#         platforms = StreamPlatform.objects.all()
#         serializer = StreamPlatformSerializer(platforms, many=True, context={'request': request}) # needed for hyperlink field in the serializer, which creates a link to the object
#         # serializer = StreamPlatformSerializer(platforms, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = StreamPlatformSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class StreamPlatformDetailView(APIView):
#     permission_classes = [IsAdminOrReadOnly]
    
#     def get_object(self, pk):
#         try:
#             return StreamPlatform.objects.get(pk=pk)
#         except StreamPlatform.DoesNotExist:
#             raise Http404
    
#     def get(self, request, pk):
#         platform = self.get_object(pk)
#         # serializer = StreamPlatformSerializer(platform)
#         serializer = StreamPlatformSerializer(platform, context={'request': request})
#         return Response(serializer.data)
    
#     def put(self, request, pk):
#         platform = self.get_object(pk)
#         serializer = StreamPlatformSerializer(platform, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)
    
#     if request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT','DELETE'])
# def movie_details(request,pk):
#     movie = None
#     try:
#         movie = Movie.objects.get(pk=pk)
#     except Movie.DoesNotExist:
#         return Response({'Error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     if request.method == 'PUT':
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     if request.method == 'DELETE':
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)