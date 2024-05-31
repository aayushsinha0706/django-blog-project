from django.db import models

from django_otp.models import (
    AbstractOTPToken,
    OTP_TOKEN_VALIDITY,
)

class OTPToken(AbstractOTPToken):
    validity = OTP_TOKEN_VALIDITY.FIVE_MINUTES
