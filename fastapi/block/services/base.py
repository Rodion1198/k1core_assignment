from typing import Protocol

import requests

from block.schemas import ServiceResult


class BlockchainService(Protocol):

    def fetch_latest_block(self, session: requests.Session, currency: str, api_key: str = None) -> ServiceResult:
        pass
