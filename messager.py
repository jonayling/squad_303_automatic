import random
import requests
from twilio.rest import Client
from config import Config

class Messager:
    USER_AGENT = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0'

    TEXTS = [
        'Уважаемые россияне, ваши СМИ подвергаются цензуре.  Кремль лжет. Узнайте правду об Украине в бесплатном Интернете и в приложении Telegram. Время свергнуть диктатора Путина!',
        'Кремль лжет!Война Путина принесла катастрофу народу России! В банках нет денег,нет топлива,все иностранные компании ушли из страны,а Путин прячется в своем дворце в Геленджике!',
        'На Украине погибло больше сынов Русского Народа, чем в Афганистане! Война Путина уничтожит Россию! Топлива нет, денег в банках нет. Путин уничтожает Россию! Кремль лжет!',
        'В Украине погибло более 10 000 сынов Русского Народа.  Кремль лжет! Путин спрятался в своем дворце в Геленджике, но денег в банках нет, топлива нет, Россия обанкротилась. Вставай!',
        'Ваши СМИ подвергаются цензуре. Кремль лжет. Ищите правду о войне в Украине в TOR:  https://www.bbcnewsd73hkzno2ini43t4gblxvycyac5aw4gnv7t2rccijh7745uqd.onion/russian или используйте приложение Psiphon.'
    ]

    def __init__(self):
        self.sms_client = Client(username=Config.account_sid, password=Config.auth_token)

    def get_russian_number(self):
        headers = {
            'User-Agent': self.USER_AGENT
        }
        response = requests.get(Config.RUSSIAN_NUMBER_API, headers=headers, cookies=Config.COOKIE)
        if response.status_code == 200:
            return response.text
        else:
            print('Failed to fetch number!')

    def send_sms(self, message, number):
        self.sms_client.messages.create(
            body=message,
            from_=Config.SMS_NUMBER,
            to=number
        )

    def run(self):
        russian_number = self.get_russian_number()
        message = random.choice(self.TEXTS)
        if russian_number:
            russian_number = '+' + russian_number
            print(f'Sending message to {russian_number}...', end='')
            self.send_sms(message, russian_number)
            print('done')
