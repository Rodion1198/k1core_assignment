from cryptography.fernet import Fernet
from django.conf import settings
from django.db import models


class EncryptedAPIKeyField(models.TextField):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fernet = Fernet(settings.ENCRYPTION_SECRET_KEY.encode())

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        return self.fernet.decrypt(value.encode()).decode()

    def get_prep_value(self, value):
        if value is None:
            return value
        return self.fernet.encrypt(value.encode()).decode()
