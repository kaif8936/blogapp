from rest_framework import serializers
from blog.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'slug', 'text', 'text_2', 'created_date', 'category', 'cover', 'cover2', 'author', 'large_heading', 'large_heading_text', 'quote', 'quotes_name', 'smaller_heading', 'smaller_heading_text', 'tag1', 'tag2', 'tag3', )