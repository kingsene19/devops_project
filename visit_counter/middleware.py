from .models import Visit
from django.urls import reverse


class VisitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == reverse("users:home"):
            visit, _ = Visit.objects.get_or_create(id=1)
            visit.number_of_visits += 1
            visit.save()
        response = self.get_response(request)
        return response
