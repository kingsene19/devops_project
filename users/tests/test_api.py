from django.test import TestCase, Client
from django.urls import reverse
from users.models import User
from users.serializers import UserSerializer

class TestAPI(TestCase):
    def setUp(self):
        self.client = Client()
        self.api_url = reverse("users:list_users")

    def testUserListIsReturned(self):
        user1 = User.objects.create(
            username="user1",
            email="user1@example.com",
            first_name="First",
            last_name="User"
        )
        user2 = User.objects.create(
            username="user2",
            email="user2@example.com",
            first_name="Second",
            last_name="User"
        )
        user1_data = UserSerializer(user1).data
        user2_data = UserSerializer(user2).data
        response = self.client.get(self.api_url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(response.data), 2)
        self.assertIn(user1_data, response.data)
        self.assertIn(user2_data, response.data)

    def testUserListShouldOnlyAllowGet(self):
        response = self.client.post(self.api_url)
        self.assertTrue(response.status_code, 405)

        response = self.client.put(self.api_url)
        self.assertTrue(response.status_code, 405)

        response = self.client.delete(self.api_url)
        self.assertTrue(response.status_code, 405)