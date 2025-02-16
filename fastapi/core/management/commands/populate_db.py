from django.conf import settings
from django.core.management.base import BaseCommand

from block.models import Currency
from provider.models import Provider


class Command(BaseCommand):
    CURRENCIES = ["BTC", "ETH"]

    # this is a public api key for sandbox. https://coinmarketcap.com/api/documentation/v1/#section/Quick-Start-Guide
    PROVIDERS = [
        {"name": "CoinMarketCap", "api_key": settings.COINMARKETCAP_API_KEY},
        {"name": "BlockChair", "api_key": ""},
    ]

    def handle(self, *args, **kwargs):
        Currency.objects.bulk_create(
            [Currency(name=name) for name in self.CURRENCIES],
            ignore_conflicts=True
        )
        Provider.objects.bulk_create(
            [Provider(name=provider['name'], api_key=provider['api_key']) for provider in self.PROVIDERS],
            ignore_conflicts=True
        )

        self.stdout.write(self.style.SUCCESS("The initial data was successfully created!"))
