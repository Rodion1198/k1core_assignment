import logging

import requests
from django.conf import settings

from block.decorators import provider_exception_handler
from block.exceptions import CoinMarketCapServiceException
from block.schemas import ServiceResult
from block.services import BlockchainService
from core.utils import send_request

logger = logging.getLogger(__name__)


class CoinMarketCapService(BlockchainService):
    """Service for CoinMarketCap (BTC)"""

    PROVIDER = 'CoinMarketCap'

    @provider_exception_handler(provider_name=PROVIDER, exception_cls=CoinMarketCapServiceException)
    def fetch_latest_block(self, session: requests.Session, currency: str, api_key: str = None) -> ServiceResult:
        if not api_key:
            error_msg = f"Missing API key for {self.PROVIDER}"
            logger.warning(error_msg)
            raise CoinMarketCapServiceException(error_msg)

        url = f"{settings.COINMARKETCAP_API_HOST}/v1/blockchain/statistics/latest?symbol=BTC"

        headers = {
            "Accepts": "application/json",
            "X-CMC_PRO_API_KEY": api_key
        }
        response = send_request(url, headers=headers, session=session)
        data = response.json()

        block_info = data.get("data", {}).get("BTC", {})
        return ServiceResult(
            block_number=block_info["total_blocks"],
        )
