from .models import Customer
from .serializers import CustomerSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def get_customer_list(request):
    if request.method == 'GET':
        customer = Customer.objects.all()
        print(customer)
        serializer = CustomerSerializer(customer, many=True)
        if len(customer) < 1:
            return Response({'data': 'no customer found'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def get_customer(request, pk):
    try:
        customer = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return Response({'data': 'customer not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        customer.delete()
        return Response({'data': 'deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
