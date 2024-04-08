from rest_framework.pagination import LimitOffsetPagination

class MyCustomLimitPagination(LimitOffsetPagination): #http://127.0.0.1:8000/api/?limit=4&myofset=3
    default_limit = 3
    limit_query_param = 'mylmt'
    offset_query_param = 'myofset'
    max_limit = 4