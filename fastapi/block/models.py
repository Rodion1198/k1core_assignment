from django.db import models

from provider.models import Provider


class Currency(models.Model):
    name = models.CharField(max_length=10, unique=True)  # BTC, ETH

    class Meta:
        verbose_name = "currency"
        verbose_name_plural = "currencies"

    def __str__(self):
        return self.name


class Block(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name="block")
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name="block")
    number = models.PositiveBigIntegerField(unique=True)
    created_at = models.DateTimeField(null=True, blank=True)
    stored_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "block"
        verbose_name_plural = "blocks"

        unique_together = ("currency", "number")

    def __str__(self):
        return f"{self.currency.name} - {self.number}"
