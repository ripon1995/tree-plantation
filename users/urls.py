from django.urls import path
from .views import CustomRegistrationView, CustomProfileView

urlpatterns = [
    path('users/', CustomRegistrationView.as_view()),
    path('users/me/', CustomProfileView.as_view())
]
