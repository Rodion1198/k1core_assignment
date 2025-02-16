from rest_framework import serializers

from block.models import Block, Currency
from provider.serializers import ProviderSerializer


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ("id", "name")


class BlockSerializer(serializers.ModelSerializer):
    currency = CurrencySerializer()
    provider = ProviderSerializer()

    class Meta:
        model = Block
        fields = ("id", "currency", "provider", "number", "created_at", "stored_at")
