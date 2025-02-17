from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def validate_title(self, value):
        if len(value) > 200:
            raise serializers.ValidationError("Заголовок не должен превышать 200 символов.")
        return value

    def validate_likes(self, value):
        if value < 0:
            raise serializers.ValidationError("Количество лайков не должно быть отрицательным.")
        return value

    def validate(self, data):
        if not data.get('title'):
            raise serializers.ValidationError("Заголовок поста не должен быть пустым.")
        if not data.get('description'):
            raise serializers.ValidationError("Описание поста не должно быть пустым.")
        return data
