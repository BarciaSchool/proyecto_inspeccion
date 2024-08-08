# miapp/middleware.py

from django.conf import settings
from django.shortcuts import redirect

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            path = request.path_info.lstrip('/')
            if not any(path.startswith(url) for url in settings.LOGIN_EXEMPT_URLS):
                return redirect(settings.LOGIN_URL)
        response = self.get_response(request)
        return response

