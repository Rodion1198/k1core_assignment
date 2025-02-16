from django.db import models

from core.fields import EncryptedAPIKeyField


class Provider(models.Model):
    name = models.CharField(max_length=100, unique=True)  # CoinMarketCap, BlockChair
    api_key = EncryptedAPIKeyField(max_length=255, blank=True)

    class Meta:
        verbose_name = "provider"
        verbose_name_plural = "providers"

    def __str__(self):
        return self.name
