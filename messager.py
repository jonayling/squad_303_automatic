import random
import requests
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

    def __init__(self, sms_service):
        self.sms_service = sms_service

    def get_russian_number(self):
        response = requests.get(Config.RUSSIAN_NUMBER_API)
        if response.status_code == 200:
            return response.text
        else:
            print('Failed to fetch number!')

    def run(self):
        russian_number = self.get_russian_number()
        message = random.choice(self.TEXTS)
        if russian_number:
            russian_number = '+' + russian_number
            print(f'Sending message to {russian_number}...', end='')
            result = self.sms_service.send_sms(message, russian_number)
            if result:
                print('done')
            else:
                print('Error!')
