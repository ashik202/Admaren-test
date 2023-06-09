from rest_framework import serializers
from .models import Tag, Snippet


class SnippetSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(read_only=True, required=False, view_name='snippets-detail')

    class Meta:
        model = Snippet
        fields = ['title', 'content', 'tag', 'timestamp', 'url']


class TagSerializer(serializers.ModelSerializer):
    snippets = SnippetSerializer(many=True, read_only=True, required=False, )

    class Meta:
        model = Tag
        fields = ['id', 'title', 'snippets']
