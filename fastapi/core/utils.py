import logging
from requests import Response, RequestException, Session
from typing import Dict, Optional, Literal, Any
from retry import retry

logger = logging.getLogger(__name__)


@retry(RequestException, tries=5, delay=2, jitter=(1, 3))
def send_request(
        url: str,
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        timeout: int = 10,
        method: Literal["GET", "POST", "PUT", "DELETE"] = "GET",
        session: Optional[Session] = None
) -> Response:

    headers = headers or {"Accepts": "application/json"}

    response = session.request(
        method=method,
        url=url,
        headers=headers,
        params=params,
        data=data,
        json=json,
        timeout=timeout,
    )
    response.raise_for_status()
    logger.info(f"Request {method} {url} - {response.status_code}")

    return response
