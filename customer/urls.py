from django.urls import path
from customer import views

urlpatterns = [
    path('customers/', views.GetCustomerList.as_view()),
    path('customers/<int:pk>/', views.GetCustomer.as_view()),
    path('customers/signup/', views.customerSignUpView),
]
