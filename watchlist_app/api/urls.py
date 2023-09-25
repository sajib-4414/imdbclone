from django.urls import path,include
from watchlist_app.api.views import (WatchListDetailView, WatchListView, 
                                    #  StreamPlatformView, StreamPlatformDetailView, 
                                     ReviewList,
                                     ReviewDetail, ReviewCreate, StreamPlatformViewSet, UserReview,
                                     WatchListSearchView
                                     )
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('stream', StreamPlatformViewSet, basename='streamplatform') #this creates, list, post
#individual get, delete, put all endpoints

urlpatterns = [
    path("list/", WatchListView.as_view(), name='movie-list'), # for class based view you need as_view()
    path('<int:pk>/', WatchListDetailView.as_view(), name='movie-detail'),
    # path('stream/', StreamPlatformView.as_view(), name='stream-list'),
    # path('stream/<int:pk>/', StreamPlatformDetailView.as_view(), name='streamplatform-detail'),
    path('',include(router.urls)),
    
    # for testing search results
    path('list2/', WatchListSearchView.as_view(), name='watch-list'),
    
    #viewsets works fine for simple tasks, but the following urls, where we have to do complex lookup and creation, 
    # non viewset views are easier to implement
    # generics.createAPIview these generic views are really powerful and also customizable
    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'), #creates a review for a particular movie
    path('<int:pk>/review/', ReviewList.as_view(), name='review-list'), #returns all reviews for a particular movie
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'), #returns a particular review of a steamed movie
    
    # path('review/', ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
    
    path('review/', UserReview.as_view(), name='user-review-detail')
    
]