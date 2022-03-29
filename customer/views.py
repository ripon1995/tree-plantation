from .models import Customer
from .serializers import CustomerSerializer, CustomerSignUpSerializer
from rest_framework import generics


class GetCustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class GetCustomer(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerSignUp(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSignUpSerializer
