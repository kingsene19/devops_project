from django.test import TestCase, Client
from django.urls import reverse
from visit_counter.models import Visit
from visit_counter.serializers import VisitSerializer

class TestAPI(TestCase):
    def setUp(self):
        self.client = Client()
        self.api_url = reverse("visits:visit_count")

    def testVisitCountIsReturned(self):
        visit = Visit.objects.create(
            number_of_visits=10
        )
        response = self.client.get(self.api_url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(response.data),1)
        self.assertIn('number_of_visits', response.data)
        self.assertEquals(response.json()["number_of_visits"], 10)

    def testVisitCountShouldOnlyAllowGet(self):
        response = self.client.post(self.api_url)
        self.assertTrue(response.status_code, 405)

        response = self.client.put(self.api_url)
        self.assertTrue(response.status_code, 405)

        response = self.client.delete(self.api_url)
        self.assertTrue(response.status_code, 405)
