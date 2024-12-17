from rest_framework import serializers
from .models import BlogPost, Comment
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ("title", "content")

    def create(self, validated_data):
        validated_data["author"] = self.context["request"].user
        return super().create(validated_data)


class BlogPostDetailedSerializer(BlogPostSerializer):
    author = serializers.ReadOnlyField(source="author.username")

    class Meta(BlogPostSerializer.Meta):
        fields = ("id", "title", "content", "author", "created_at", "updated_at")


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("content", "post")
        read_only_fields = ("commenter_name",)

    # def validate(self, data):
    #     """
    #     Check if the user has already commented on this post.
    #     """
    #     user = self.context["request"].user
    #     post = data.get("post")

    #     # Check for an existing comment by this user on this post
    #     if Comment.objects.filter(post=post, commenter_name=user).exists():
    #         raise serializers.ValidationError(
    #             {"detail": "You can only comment once on this post."}
    #         )

    #     return data

    def create(self, validated_data):
        """
        Set the commenter_name to the logged-in user.
        """
        validated_data["commenter_name"] = self.context["request"].user
        return super().create(validated_data)


class ViewDetailedCommentSerializer(serializers.ModelSerializer):
    post = BlogPostSerializer(read_only=True)
    commenter_name = serializers.ReadOnlyField(source="commenter_name.username")
    commenter_id = serializers.ReadOnlyField(source="commenter_name.id")

    class Meta:
        model = Comment
        fields = [
            "id",
            "post",
            "commenter_name",
            "commenter_id",
            "content",
            "created_at",
        ]
        read_only_fields = ("commenter_name", "commenter_id")


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email"),
            password=validated_data["password"],
        )
        return user


class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
