from django.urls import path
from .views import CustomRegistrationView

urlpatterns = [
    path('users/', CustomRegistrationView.as_view()),
]
