import requests
from django.conf import settings

from block.decorators import provider_exception_handler
from block.exceptions import BlockChairServiceException
from block.schemas import ServiceResult
from block.services import BlockchainService
from core.utils import send_request


class BlockChairService(BlockchainService):
    """Service for BlockChair (ETH)"""

    PROVIDER = 'BlockChair'

    @provider_exception_handler(provider_name=PROVIDER, exception_cls=BlockChairServiceException)
    def fetch_latest_block(self, session: requests.Session, currency: str, api_key: str = None) -> ServiceResult:
        url = f"{settings.BLOCKCHAIR_API_HOST}/ethereum/stats"

        response = send_request(url, session=session)
        data = response.json()

        block_info = data.get("data", {})
        return ServiceResult(
            block_number=block_info["best_block_height"],
            created_at=block_info.get("best_block_time")
        )
