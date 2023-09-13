from django.test import SimpleTestCase
from django.urls import resolve, reverse
from visit_counter.api import count_visits


class TestUrls(SimpleTestCase):
    def testVisitCountUrlResolves(self):
        url = reverse("visits:visit_count")
        self.assertEquals(resolve(url).func, count_visits)
