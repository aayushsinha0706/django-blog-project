from django import forms
from django_otp.forms import OTPPasswordTokenForm

class OTPForm(OTPPasswordTokenForm):
    pass

class LoginForm(OTPPasswordTokenForm):
    pass