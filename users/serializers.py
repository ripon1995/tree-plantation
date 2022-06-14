from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers


class UsersCreateSerializer(UserCreateSerializer):

    class Meta(UserCreateSerializer.Meta):
        model = get_user_model()
        fields = ['id', 'email', 'name', 'username', 'password', 'phone']

    def to_representation(self, instance):
        representation = super(UserCreateSerializer, self).to_representation(instance)
        body = {'body': representation, 'message': 'success'}
        return body
