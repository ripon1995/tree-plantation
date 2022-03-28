from django.urls import path
from customer import views

urlpatterns = [
    path('customers/', views.get_customer_list),
    path('customers/<int:pk>/', views.get_customer)
]
