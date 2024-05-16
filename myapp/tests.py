from django.test import TestCase
from django.urls import reverse
from .models import MyModel

class MyModelTestCase(TestCase):
    def setUp(self):
        MyModel.objects.create(name="Test Name")

    def test_model_creation(self):
        obj = MyModel.objects.get(name="Test Name")
        self.assertEqual(obj.name, "Test Name")

    def test_view_response(self):
        response = self.client.get(reverse('myapp:index'))
        self.assertEqual(response.status_code, 200)
