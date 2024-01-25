from django.contrib.auth import get_user_model
from rest_framework import serializers

from posts.models import Comment, Post, Group, Follow
from rest_framework.validators import UniqueTogetherValidator

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True
    )
    group = serializers.PrimaryKeyRelatedField(
        queryset=Group.objects.all(), required=False
    )

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date', 'group')
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = ('id', 'text', 'post', 'created', 'author')
        model = Comment
        read_only_fields = ('post',)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        read_only=False, slug_field='username', queryset=User.objects.all())

    class Meta:
        fields = ('id', 'following', 'user')
        model = Follow
        read_only_fields = ('user',)
        validators = [UniqueTogetherValidator(
            queryset=Follow.objects.all(),
            fields=['user', 'following']
        )]

    def validate_following(self, data):
        if self.context['request'].user == data:
            raise serializers.ValidationError(
                'подписаться на самого себя нельзя!')
        return data
