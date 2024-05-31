from django.shortcuts import render, redirect
from two_factor.views import OTPRequiredMixin, LoginView
from django.urls import reverse_lazy
from django.views.generic import TemplateView


class OTPView(OTPRequiredMixin, TemplateView):
    template_name = 'otp/otp_view.html'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        return reverse_lazy('otp:otp')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['otp_required'] = True
        return context