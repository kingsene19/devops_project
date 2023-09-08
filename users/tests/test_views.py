from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.home_url = reverse("users:home")
        self.home_template = "users/home.html"

    def testHomeShouldReturnHomePage(self):
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateNotUsed(self.home_template)
