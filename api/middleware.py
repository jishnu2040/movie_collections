from django.utils.deprecation import MiddlewareMixin
from threading import Lock

class RequestCountMiddleware(MiddlewareMixin):
    request_count = 0
    lock = Lock()

    def process_request(self, request):
        with self.lock:
            RequestCountMiddleware.request_count += 1
