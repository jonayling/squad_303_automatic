from abc import abstractmethod, ABC


class BaseSmsService(ABC):

    @abstractmethod
    def send_sms(self, message, number):
        pass
