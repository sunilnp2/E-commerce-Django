from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination, CursorPagination

class MyPageNumPagination(PageNumberPagination):
    page_size = 5
    max_page_size = 7
    # last_page_strings = "end"

# for CursorPagination

class MyCursorPagination(CursorPagination):
    page_size  = 5
    ordering = "name"
    max_page_size = 7

class UserCursorPagination(CursorPagination):
    page_size  = 5
    ordering = "username"
    max_page_size = 7