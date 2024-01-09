from django.contrib.auth.mixins import UserPassesTestMixin
from kavenegar import *
import ghasedakpack

# create an instance:
sms = ghasedakpack.Ghasedak("06899ddf184ede60a94e6f40acfb7dfec7e83df665ebd3c6f33ebdba8571700e")


def send_otp_code(phone_number, code):
    template = 'Maktab_Sharif Cafe confirmation code '  # Replace with your actual template

    # Construct the parameters for the SMS
    params = {
        'receptor': phone_number,
        'type': '1',  # Assuming '1' is the type for SMS verification, adjust if needed
        'template': template,
        'param1': code,
        'param2': '',  # Add additional parameters if needed
        'param3': ''
    }

    # Call the SMS verification service
    sms.verification(params)


class IsAdminUserMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_admin
