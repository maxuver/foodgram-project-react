from rest_framework.pagination import PageNumberPagination


class ProjectPagination(PageNumberPagination):
    page_size_query_param = 'limit'
