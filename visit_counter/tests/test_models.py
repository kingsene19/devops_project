from django.test import TestCase
from visit_counter.models import Visit


class TestModel(TestCase):
    def setUp(self):
        self.visit = Visit.objects.create(number_of_visits=1)

    def testVisitIsCreated(self):
        visits = Visit.objects.all()
        self.assertTrue(isinstance(self.visit, Visit))
        self.assertEquals(visits[0].number_of_visits, self.visit.number_of_visits)

    def testVerboseNamesValues(self):
        self.assertEqual(Visit._meta.verbose_name, "Visit")
        self.assertEqual(Visit._meta.verbose_name_plural, "Visits")

    def testStrIsCalled(self):
        self.assertEqual(str(self.visit), f"Visit object ({self.visit.id})")
