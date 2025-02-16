import logging

import requests
from celery import shared_task
from django.utils import timezone

from block.models import Currency, Block
from block.schemas import ServiceResult
from block.services import ServiceFactory, BlockchainService
from provider.models import Provider

logger = logging.getLogger(__name__)


@shared_task
def fetch_latest_block():
    with requests.Session() as session:

        currencies = Currency.objects.all()

        for currency in currencies:
            # This filter is necessary just to immediately take services that support the desired currency.
            providers = Provider.objects.filter(name__in=ServiceFactory.SERVICES.get(currency.name, {}))
            for provider in providers:
                try:
                    service: BlockchainService = ServiceFactory.get_service(provider.name, currency.name)
                    result: ServiceResult = service.fetch_latest_block(
                        session=session,
                        currency=currency.name,
                        api_key=provider.api_key
                    )
                    Block.objects.get_or_create(
                        currency=currency,
                        number=result.block_number,
                        defaults={
                            "provider": provider,
                            "created_at": result.created_at,
                            "stored_at": timezone.now(),
                        }
                    )

                except Exception as e:
                    print(str(e))
                    logger.error(str(e))
