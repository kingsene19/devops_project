from django.test import TestCase
from visit_counter.models import Visit
from visit_counter.serializers import VisitSerializer

class TestSerializers(TestCase):
    def setUp(self):
        self.visit_data = {
            "number_of_visits": 1
        }
        self.serializer = VisitSerializer(data=self.visit_data)

    def testSerializerIsValid(self):
        self.assertTrue(self.serializer.is_valid())

    def testSerializerShouldCreateVisitWhenSaved(self):
        self.serializer.is_valid()
        visit_instance = self.serializer.save()
        self.assertIsInstance(visit_instance, Visit)

    def testSerializerShouldContainVisitFields(self):
        self.assertTrue(self.serializer.is_valid())
        data = self.serializer.data
        self.assertEqual(
            set(data.keys()), {"number_of_visits"}
        )