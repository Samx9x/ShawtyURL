import logging
import requests
from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger(__name__)

class LoggingMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        try:
            log_data = {
                "stack": "backend",
                "level": "info" if response.status_code < 400 else "error",
                "package": "middleware",
                "message": f"{request.method} {request.path} -> {response.status_code}"
            }
            # Send to evaluation-service logs API
            requests.post(
                "http://20.244.56.144/evaluation-service/logs",
                json=log_data,
                timeout=2
            )
        except Exception as e:
            logger.error(f"Logging failed: {e}")
        return response
