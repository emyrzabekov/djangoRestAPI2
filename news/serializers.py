from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import News


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username',]

# Зачем в этом классе вытащили отдельно два поля и остальные в Мета класс загнали..????
class NewsSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField()
    owner = UserSerializer(read_only=True)

    class Meta:
        model = News
        fields = ['id', 'owner', 'title', 'body', 'img', 'created_at', 'active']
        read_only_fields = ['created_at',]