from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    @staticmethod
    def validate_title(value: str) -> str:
        if len(value) > 200:
            raise serializers.ValidationError("Заголовок не должен превышать 200 символов.")
        return value

    @staticmethod
    def validate_likes(value: int) -> int:
        if value < 0:
            raise serializers.ValidationError("Количество лайков не должно быть отрицательным.")
        return value

    @staticmethod
    def validate_not_empty(data: object) -> object:
        if not data.get('title'):
            raise serializers.ValidationError("Заголовок поста не должен быть пустым.")
        if not data.get('description'):
            raise serializers.ValidationError("Описание поста не должно быть пустым.")
        return data
