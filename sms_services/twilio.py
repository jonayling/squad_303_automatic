from .base_sms_service import BaseSmsService
from twilio.rest import Client
from config import Config


class TwilioSmsService(BaseSmsService):

    def __init__(self):
        self.sms_client = Client(username=Config.account_sid, password=Config.auth_token)

    def send_sms(self, message, number):
        self.sms_client.messages.create(
            body=message,
            from_=Config.SMS_NUMBER,
            to=number
        )
