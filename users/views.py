from .serializers import UsersCreateSerializer, UserProfileSerializer
from rest_framework import generics, viewsets
from rest_framework.response import Response
from .models import UserAccount


class CustomRegistrationView(generics.CreateAPIView):
    serializer_class = UsersCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        valid = serializer.is_valid()
        if not valid:
            data = {'message': 'fail', 'data': {key: val[0].title() for key, val in serializer.errors.items()}}
            return Response(data=data)

        response = super().create(request, *args, **kwargs)
        data = {'message': 'success', 'data': response.data}
        return Response(data=data)


class CustomProfileView(generics.RetrieveAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = UserProfileSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.queryset.filter(pk=request.user.id).first()
        serializer = self.get_serializer(request.user)

        return Response({"message": "success", "data": serializer.data})
