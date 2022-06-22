from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from django.contrib.auth import get_user_model


class UsersCreateSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        model = get_user_model()
        fields = ['id', 'email', 'name', 'username', 'password', 'phone']

    def to_representation(self, instance):
        representation = super(BaseUserRegistrationSerializer, self).to_representation(instance)
        custom_success_response = {'message': 'success', 'body': representation, }
        return custom_success_response
