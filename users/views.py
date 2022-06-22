
from .serializers import UsersCreateSerializer
from rest_framework import generics
from rest_framework.response import Response


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
