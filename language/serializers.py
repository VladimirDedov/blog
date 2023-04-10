from rest_framework import serializers

from .models import *

class BlogListSerialiser(serializers.ModelSerializer):
    """List of blog of articles"""
    category = serializers.SlugRelatedField(slug_field='category', read_only=True)
    class Meta:
        model = Blog
        fields=('title','slug', 'content','date_add', 'category', 'image_1')

class BlogDetailSerialiser(serializers.ModelSerializer):
    """Detail articles"""

    category = serializers.SlugRelatedField(slug_field='category', read_only=True)
    class Meta:
        model = Blog
        exclude = ('is_published',)

class DictListSerializer(serializers.ModelSerializer):
    """List of words"""
    class Meta:
        model = Distionary
        fields = '__all__'

class WordDetailSerializer(serializers.ModelSerializer):
    """Detail word"""

    class Meta:
        model = Distionary
        fields = "__all__"