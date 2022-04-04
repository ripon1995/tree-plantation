from .models import Customer
from .serializers import CustomerSerializer, CustomerSignUpSerializer
from rest_framework import generics
from rest_framework.response import Response


class GetCustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class GetCustomer(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerSignUp(generics.CreateAPIView):
    serializer_class = CustomerSignUpSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        valid = serializer.is_valid()
        if not valid:
            data = {
                'message': 'fail',
                'data': serializer.errors
            }
            return Response(data=data)
        response = super().create(request, *args, **kwargs)
        data = {
            'message': 'success',
            'data': response.data
        }
        return Response(data=data)
