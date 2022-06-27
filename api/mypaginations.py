from rest_framework.pagination import CursorPagination

class myCursorPagination(CursorPagination):
    page_size = 3
    ordering = 'name'
    max_page_size = 6