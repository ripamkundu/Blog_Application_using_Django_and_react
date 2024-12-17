from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import (
    ListCreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
)
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from blog.models import BlogPost, Comment
from blog.serializers import (
    BlogPostDetailedSerializer,
    BlogPostSerializer,
    CommentSerializer,
    RegisterUserSerializer,
    LoginUserSerializer,
    ViewDetailedCommentSerializer,
)


class RegisterUserView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "user": serializer.data,
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                }
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginUserView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "userid": user.id,
                    "username": user.username,
                    "email": user.email,
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                }
            )
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


# Create new Blog Uisng this generic View
class BlogPosCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BlogPostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# View all Blogs
class BlogPostListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BlogPostDetailedSerializer

    def get_queryset(self):
        return BlogPost.objects.all().order_by("-created_at")


# Retrive single Blog / Update / Delete
class BlogPostDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BlogPostSerializer
    queryset = BlogPost.objects.all()

    # Only the author of the blog can update it
    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.author != request.user:
            return Response(
                {
                    "message": "Only the author of the blog can update it",
                },
                status=status.HTTP_403_FORBIDDEN,
            )
        return super().update(request, *args, **kwargs)

    # Only the author of the blogand adin can delete it
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.author != request.user and not request.user.is_superuser:
            return Response(
                {
                    "message": "Only the author of the blog and admin can delete it",
                },
                status=status.HTTP_403_FORBIDDEN,
            )
        return super().destroy(request, *args, **kwargs)


# Create new comment
class CommentCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer


# list of all comments of a blog by blog id
class CommentListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ViewDetailedCommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(post=self.kwargs["pk"]).order_by("-created_at")


class CommentDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ViewDetailedCommentSerializer
    queryset = Comment.objects.all()

    # Only the author of the comment can update it
    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.commenter_name != request.user:
            return Response(
                {"message": "Only the author of the comment can update it"},
                status=status.HTTP_403_FORBIDDEN,
            )
        return super().update(request, *args, **kwargs)

    # Only the author of the comment or admin can delete it
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.commenter_name != request.user and not request.user.is_superuser:
            return Response(
                {"message": "Only the author of the comment or an admin can delete it"},
                status=status.HTTP_403_FORBIDDEN,
            )
        return super().destroy(request, *args, **kwargs)
