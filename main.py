import schedule
import time
from messager import Messager
from config import Config


if __name__ == '__main__':
    messager = Messager()

    schedule.every(Config.MESSAGE_FREQUENCY).seconds.do(messager.run)
    while True:
        schedule.run_pending()
        time.sleep(1)
