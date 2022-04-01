from .models import Customer
from .serializers import CustomerSerializer, CustomerSignUpSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


class GetCustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class GetCustomer(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerSignUp(generics.CreateAPIView):

    def create(self, request, *args, **kwargs):
        serializer_class = CustomerSignUpSerializer
        if not self.serializer_class.is_valid(raise_exception=False):
            return Response({"message": "invalid"}, {"errors": serializer_class.errors})

        self.perform_create(serializer_class)
        headers = self.get_success_headers(serializer_class.data)
        serializer_class.save()
        return Response({"message": "success"}, {"data": serializer_class.data}, headers=headers)


@api_view(['POST'])
def customerSignUpView(request):
    if request.method == 'POST':
        serializer = CustomerSignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "success"}, status=status.HTTP_201_CREATED)
        data = {'message': 'fail', 'body': serializer.errors}
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
