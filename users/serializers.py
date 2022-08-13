from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from djoser.serializers import UserSerializer as Profile
from django.contrib.auth import get_user_model


class UsersCreateSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        model = get_user_model()
        fields = ['id', 'email', 'name', 'username', 'password', 'phone']


class UserProfileSerializer(Profile):
    class Meta(Profile.Meta):
        model = get_user_model()
        fields = ['id', 'email', 'name', 'username', 'phone']
