from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class MovieListPagination(PageNumberPagination):
    page_size = 4
    # page_query_param = 'p'
    page_size_query_param = 'page_size'
    max_page_size = 7
    last_page_strings = 'end'
    
class MovieListLimitOffsetPagination(LimitOffsetPagination):
    default_limit  = 5
    max_limit = 6
    limit_query_param = 'limit' # to customize what the parametter will be called
    offset_query_param = 'start' # to customize what the parametter will be called
    
class MovieListCursorPagination(CursorPagination):
    page_size = 5
    ordering = 'created' # created means ascending order with created. by default its -created, which is
    # descedning with created.