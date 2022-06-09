from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model


class UsersCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = get_user_model()
        fields = ['id', 'email', 'name', 'username', 'password', 'phone']
