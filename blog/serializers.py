from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Post, Comment, Snippet, LANGUAGE_CHOICES

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'pk', 'username', 'groups', 'snippets', 'posts')

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
   
    class Meta:
        model = Snippet
        fields = ('url', 'pk', 'owner',
                  'title', 'code', 'linenos', 'language')

class PostSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
   
    class Meta:
        model = Post
        fields = ('url', 'pk', 'owner',
                  'title', 'text', 'created_date', 'published_date')