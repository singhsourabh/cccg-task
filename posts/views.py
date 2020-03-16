from rest_framework import generics
from .serializers import PostSerializer
from .models import Post
from rest_framework import filters


class PostList(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['view_count', 'score']
    search_fields = ['title', 'body']
