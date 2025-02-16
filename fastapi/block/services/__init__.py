from typing import Type

from block.services.base import BlockchainService
from block.services.blockchair import BlockChairService
from block.services.coinmarketcap import CoinMarketCapService


class ServiceFactory:
    # The condition of the assignment was that CoinMarketCap service should work for BTC, and BlockChair only for ETH.
    # It can be easily extended or removed for a more flexible approach.
    SERVICES: dict[str, dict[str, Type[BlockchainService]]] = {
        "BTC": {CoinMarketCapService.PROVIDER: CoinMarketCapService},
        "ETH": {BlockChairService.PROVIDER: BlockChairService},
    }

    @classmethod
    def get_service(cls, provider_name: str, currency_name: str) -> BlockchainService:
        if currency_name not in cls.SERVICES or provider_name not in cls.SERVICES[currency_name]:
            raise ValueError(f"Unsupported provider {provider_name} for currency {currency_name}")

        return cls.SERVICES[currency_name][provider_name]()
