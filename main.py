import schedule
import time
from messager import Messager
from config import Config
from sms_services.bulk_sms import BulkSmsService


if __name__ == '__main__':
    sms_service = BulkSmsService()
    messager = Messager(sms_service)

    schedule.every(Config.MESSAGE_FREQUENCY).seconds.do(messager.run)
    while True:
        schedule.run_pending()
        time.sleep(1)
