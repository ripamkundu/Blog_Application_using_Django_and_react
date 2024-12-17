from django.urls import path
from .views import (
    RegisterUserView,
    LoginUserView,
    BlogPosCreateView,
    BlogPostListView,
    BlogPostDetailView,
    CommentCreateView,
    CommentListView,
    CommentDetailView,
)
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("api/register/", RegisterUserView.as_view(), name="register"),
    path("api/login/", LoginUserView.as_view(), name="login"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/post/", BlogPosCreateView.as_view(), name="post-create"),
    path("api/posts/", BlogPostListView.as_view(), name="post-list"),
    path("api/posts/<int:pk>/", BlogPostDetailView.as_view(), name="post-detail"),
    path("api/comments/", CommentCreateView.as_view(), name="comment-create"),
    path("api/comments/post/<int:pk>/", CommentListView.as_view(), name="comment-list"),
    path("api/comments/<int:pk>/", CommentDetailView.as_view(), name="comment-detail"),
]
