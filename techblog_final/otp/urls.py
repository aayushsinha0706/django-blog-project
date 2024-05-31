# urls.py
from django.urls import path
from .views import OTPView, CustomLoginView

app_name = 'otp'
urlpatterns = [
    path('otp/', OTPView.as_view(), name='otp'),
    path('login/', CustomLoginView.as_view(), name='login'),
]