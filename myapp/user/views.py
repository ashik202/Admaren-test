from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from .models import Tag, Snippet
from .serializers import TagSerializer, SnippetSerializer

# Create your views here.
"""This is the view for creating Snippets"""


class SnippetListCreateView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SnippetSerializer

    @extend_schema(responses=SnippetSerializer)
    def post(self, request):
        tag_title = request.data.get('tag')
        tag_object, _ = Tag.objects.get_or_create(title=tag_title)
        serializer_data = request.data.copy()
        serializer_data['tag'] = tag_object.pk

        serializer = SnippetSerializer(data=serializer_data)
        if serializer.is_valid():
            serializer.save(created_user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


"""This the view  for showing Snippet Details"""


class SnippetDetailedView(APIView):
    @extend_schema(responses=SnippetSerializer)
    def get(self, request, pk=None):
        snippet = get_object_or_404(Snippet, pk=pk)
        serializer = SnippetSerializer(snippet, context={'request': request})
        return Response(serializer.data)


"""This is the View for updating and deleting a snippet"""


class SnippetUpdateDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(responses=SnippetSerializer)
    def put(self, request, pk=None):
        tag = request.data.get('tag')
        user = request.user
        tag_object, _ = Tag.objects.get_or_create(title=tag)
        serializer_data = request.data.copy()
        serializer_data['tag'] = tag_object.pk

        snippet = get_object_or_404(Snippet, pk=pk)
        serializer = SnippetSerializer(snippet, data=serializer_data)
        if serializer.is_valid():
            serializer.save(tag=tag_object, created_user=user)
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk=None):
        snippet = get_object_or_404(Snippet, pk=pk)
        snippet.delete()
        return Response(status=204)


"""This is the view used to list all tags"""


class TagListView(APIView):
    @extend_schema(responses=TagSerializer)
    def get(self, request):
        tag_obj = Tag.objects.all().values('title')
        serializer = TagSerializer(tag_obj, many=True, )
        return Response(serializer.data)


"""This the view for Tag Details"""


class TagDetailView(APIView):
    @extend_schema(responses=TagSerializer)
    def get(self, request, pk=None):
        snippet = get_object_or_404(Tag, pk=pk)
        serializer = TagSerializer(snippet, context={'request': request})
        return Response(serializer.data)


"""This is the View for giving overview of all snippets"""


class SnippetOverview(APIView):
    @extend_schema(responses=SnippetSerializer)
    def get(self, request):
        snippet_count = Snippet.objects.count()
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True, context={'request': request})
        snippet_list = serializer.data

        response_data = {
            'snippet_count': snippet_count,
            'snippets': snippet_list
        }

        return Response(response_data)
