import requests
import json
from requests.auth import HTTPBasicAuth
from .base_sms_service import BaseSmsService
from config import Config


class BulkSmsService(BaseSmsService):

    FROM_NUMBER = 'information'

    def __init__(self):
        pass

    def send_sms(self, message, number):
        data = {
            'from': self.FROM_NUMBER,
            'to': number,
            'body': message,
            'encoding': 'UNICODE'
        }
        headers = {
            'Content-Type': 'application/json; charset=utf-8'
        }
        payload = json.dumps(data, ensure_ascii=False)
        auth = HTTPBasicAuth(Config.bulk_username, Config.bulk_password)
        response = requests.post(Config.bulk_sms_api, payload.encode('utf-8'), auth=auth, headers=headers)
        return response.status_code == 201
