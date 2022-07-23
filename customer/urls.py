from django.urls import path
from customer import views

urlpatterns = [
    path('details/', views.CreateCustomerDetails.as_view()),
    path('details/<int:pk>/', views.GetCustomerDetails.as_view())
]
