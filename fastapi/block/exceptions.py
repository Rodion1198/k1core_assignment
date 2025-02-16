from fastapi import HTTPException, status


class BlockNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail="Block not found")


class ServiceException(Exception):
    """Base exception for service errors."""

    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


class CoinMarketCapServiceException(ServiceException):
    """Exception for CoinMarketCap service."""

    def __init__(self, message: str):
        super().__init__(message)


class BlockChairServiceException(ServiceException):
    """Exception for BlockChair service."""

    def __init__(self, message: str):
        super().__init__(message)
