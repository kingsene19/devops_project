from django.test import TestCase
from users.models import User


class TestModels(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="jdoe123",
            email="test@example.com",
            first_name="John",
            last_name="Doe",
        )

    def testUserIsCreated(self):
        users = User.objects.all()
        self.assertTrue(isinstance(self.user, User))
        self.assertEquals(users[0].username, self.user.username)
        self.assertEquals(users[0].email, self.user.email)
        self.assertEquals(users[0].first_name, self.user.first_name)
        self.assertEquals(users[0].last_name, self.user.last_name)

    def testStrIsCalled(self):
        self.assertEquals(
            str(self.user), f"{self.user.first_name} {self.user.last_name}"
        )

    def testVerboseNamesValues(self):
        self.assertEqual(User._meta.verbose_name, "User")
        self.assertEqual(User._meta.verbose_name_plural, "Users")

    def testEmailHelpText(self):
        field = User._meta.get_field("email")
        self.assertEqual(field.help_text, "Entrer votre mail")

    def testUsernameMaxLength(self):
        field = User._meta.get_field("username")
        self.assertEqual(field.max_length, 255)

    def testEmailMaxLength(self):
        field = User._meta.get_field("email")
        self.assertEqual(field.max_length, 254)

    def testFirstNameMaxLength(self):
        field = User._meta.get_field("first_name")
        self.assertEqual(field.max_length, 255)

    def testLastNameMaxLength(self):
        field = User._meta.get_field("last_name")
        self.assertEqual(field.max_length, 255)
