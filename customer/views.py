from .models import Customer
from .serializers import CustomerSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class CreateCustomerDetails(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CustomerSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        valid = serializer.is_valid()
        if not valid:
            data = {'message': 'fail', 'data': {key: val[0].title() for key, val in serializer.errors.items()}}
            return Response(data=data)

        response = super().create(request, *args, **kwargs)
        data = {'message': 'success', 'data': response.data}
        return Response(data=data)


class GetCustomerDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    # retrieve endpoint
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({"message": "success", "data": serializer.data})

    # update endpoint added
    def update(self, request, *args, **kwargs):
        super(GetCustomerDetails, self).update(request, *args, **kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({"message": "success", "data": serializer.data})
