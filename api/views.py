from rest_framework import generics, permissions
from blog.models import Post
from .serializers import PostSerializer

class PostAPIView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostAPIDetailView(generics.ListCreateAPIView):
    
    queryset = Post.objects.all()
    serializer_class = PostSerializer
