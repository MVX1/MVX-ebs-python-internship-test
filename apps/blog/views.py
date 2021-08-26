from rest_framework import viewsets
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from apps.blog.models import Category, Blog,Comment
from apps.blog.serializers import CategorySerializer, BlogSerializer,CommentSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    authentication_classes = ()
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class BlogListView(GenericAPIView):
    serializer_class = BlogSerializer

    permission_classes = (AllowAny,)
    authentication_classes = ()

    def get(self, request):
        blogs = Blog.objects.all()

        return Response(BlogSerializer(blogs, many=True).data)


class BlogItemView(GenericAPIView):
    serializer_class = BlogSerializer

    permission_classes = (AllowAny,)
    authentication_classes = ()

    def get(self, request, pk):
        blog = get_object_or_404(Blog.objects.filter(pk=pk))
        comments = Comment.objects.filter(blog=pk)
        return Response(CommentSerializer(comments,many=True).data)


class BlogViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    authentication_classes = ()
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()

class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    authentication_classes = ()
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()