from django.test import SimpleTestCase
from django.urls import resolve, reverse
from users.views import home
from users.api import list_users


class TestUrls(SimpleTestCase):
    def testHomeUrlResolves(self):
        url = reverse("users:home")
        self.assertEquals(resolve(url).func, home)

    def testListUsersUrlResolves(self):
        url = reverse("users:list_users")
        self.assertEquals(resolve(url).func, list_users)
