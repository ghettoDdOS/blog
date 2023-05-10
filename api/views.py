from rest_framework import decorators, generics, mixins, permissions, viewsets

from api import permissions as api_permissions
from api.models import Author, Blog, Comment
from api.serializers import AuthorSerializer, BlogSerializer, CommentSerializer


class AuthorRegistrationView(generics.CreateAPIView):
    serializer_class = AuthorSerializer
    permission_classes = [permissions.AllowAny]


class AuthorProfileView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class AuthorListView(generics.ListAPIView):
    queryset = Author.objects.all().order_by("-date_joined")
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated]


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all().order_by("-created_at")
    serializer_class = BlogSerializer

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ("create", "retrieve", "list"):
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [
                permissions.IsAuthenticated,
                api_permissions.IsAuthorOrReadOnly,
            ]
        return [permission() for permission in permission_classes]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by("-created_at")
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ("create", "retrieve", "list"):
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [
                permissions.IsAuthenticated,
                api_permissions.IsAuthorOrReadOnly,
            ]
        return [permission() for permission in permission_classes]
