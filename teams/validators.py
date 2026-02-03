from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class LogoValidator:
    def __init__(self, size_mb :int , message :str = None):
        self.size_mb = size_mb
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if not value:
            self.__message = f"Logo size should be less than {self.size_mb} MB"
        else:
            self.__message = value

    def __call__(self, value):
        if value.size > self.size_mb * 1024 * 1024:
            raise ValidationError(self.message)

