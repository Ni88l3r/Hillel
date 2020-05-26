from time import time

from teachers.models import Logger


class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == "/admin/":
            request_time = time()
            response = self.get_response(request)
            response_time = time()
            response_processing_time = response_time - request_time
            log_entry = Logger(method=request.method, path=request.path, execution_time=response_processing_time)
            log_entry.save()
        else:
            response = self.get_response(request)
        return response
