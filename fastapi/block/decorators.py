import logging
from functools import wraps
from json import JSONDecodeError
from typing import Type

from requests import RequestException

logger = logging.getLogger(__name__)


def provider_exception_handler(provider_name: str, exception_cls: Type[Exception]):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except RequestException as e:
                error_msg = f"Network error while fetching from {provider_name}: {str(e)}"
                logger.error(error_msg, exc_info=True)
                raise exception_cls(error_msg)
            except JSONDecodeError as e:
                error_msg = f"Failed to parse JSON from {provider_name}: {str(e)}"
                logger.error(error_msg, exc_info=True)
                raise exception_cls(error_msg)
            except Exception as e:
                error_msg = f"Unexpected error in {provider_name}: {str(e)}"
                logger.error(error_msg, exc_info=True)
                raise

        return wrapper

    return decorator
