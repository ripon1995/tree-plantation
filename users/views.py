from .serializers import UsersCreateSerializer, UserProfileSerializer
from rest_framework import generics
from rest_framework.response import Response
from .models import UserAccount
from rest_framework.permissions import IsAuthenticated, AllowAny


class CustomRegistrationView(generics.CreateAPIView):
    permission_classes = [AllowAny]
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
    permission_classes = [IsAuthenticated]
    queryset = UserAccount.objects.all()
    serializer_class = UserProfileSerializer

    def retrieve(self, request, *args, **kwargs):
        queryset = self.queryset.filter(pk=request.user.id).first()
        serializer = self.get_serializer(request.user)
        return Response({"message": "success", "detail": serializer.data})
