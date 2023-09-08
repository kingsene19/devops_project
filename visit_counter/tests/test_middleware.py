from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from visit_counter.models import Visit
from visit_counter.middleware import VisitMiddleware

class VisitMiddlewareTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.home_url = reverse("users:home")
        self.api_url = reverse("users:list_users")

    def testMiddlewareIncreaseVisitCountOnHomeRequest(self):
        def get_count(request):
            return Visit.objects.all()[0].number_of_visits
        visit,_ = Visit.objects.get_or_create(id=1)
        visit_count_before = visit.number_of_visits
        middleware = VisitMiddleware(get_count)
        request = self.factory.get(self.home_url)
        response = middleware(request)
        self.assertEqual(response, visit_count_before +1)

    def testMiddlewareDoesNotIncreaseCounForOtherPaths(self):
        def get_count(request):
            return Visit.objects.all()[0].number_of_visits
        visit,_ = Visit.objects.get_or_create(id=1)
        visit_count_before = visit.number_of_visits
        middleware = VisitMiddleware(get_count)
        request = self.factory.get(self.api_url)
        response = middleware(request)
        self.assertEqual(response, visit_count_before)

    def test_middleware_passes_request_to_next_middleware(self):
        def mock_get_response(request):
            return "Mock Response"
        middleware = VisitMiddleware(mock_get_response)
        request = self.factory.get(reverse("users:home"))
        response = middleware(request)
        self.assertEqual(response, "Mock Response")

