from django.test import TestCase
from users.models import User
from users.serializers import UserSerializer


class TestSerializers(TestCase):
    def setUp(self):
        self.user_data = {
            "username": "jdoe123",
            "email": "test@example.com",
            "first_name": "John",
            "last_name": "Doe",
        }

        self.serializer = UserSerializer(data=self.user_data)

    def testSerializerIsValid(self):
        self.assertTrue(self.serializer.is_valid())

    def testSerializerShouldCreateUserWhenSaved(self):
        self.serializer.is_valid()
        user_instance = self.serializer.save()
        self.assertIsInstance(user_instance, User)

    def testSerializerShouldContainUserFields(self):
        self.assertTrue(self.serializer.is_valid())
        data = self.serializer.data
        self.assertEqual(
            set(data.keys()), {"username", "email", "first_name", "last_name"}
        )
