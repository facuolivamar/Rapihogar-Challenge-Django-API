import json
from rapihogar.models import User
from django.urls import reverse

from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rapihogar.models import Tecnico


class TecnicoListAPIViewTestCase(APITestCase):
    url = reverse("tecnico")

    def setUp(self):
        self.username = "user_test"
        self.email = "test@rapihogar.com"
        self.password = "Rapi123"
        self.user = User.objects.create_user(self.username, self.email, self.password, first_name="Test", last_name="User")
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

        # Crear datos de prueba para técnicos
        self.tecnico1 = Tecnico.objects.create(first_name="Juan", last_name="Perez")
        self.tecnico2 = Tecnico.objects.create(first_name="Ana", last_name="Lopez")

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_list_tecnicos(self):
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(len(json.loads(response.content)), Tecnico.objects.count())

class TecnicoReportAPIViewTestCase(APITestCase):
    url = reverse("tecnico/informe")

    def setUp(self):
        # Crear usuario de prueba y autenticación
        self.username = "user_test"
        self.email = "test@rapihogar.com"
        self.password = "Rapi123"
        self.user = User.objects.create_user(self.username, self.email, self.password, first_name="Test", last_name="User")
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

        # Crear datos de prueba para técnicos
        self.tecnico1 = Tecnico.objects.create(first_name="Juan", last_name="Perez")
        self.tecnico2 = Tecnico.objects.create(first_name="Ana", last_name="Lopez")

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_tecnico_report(self):
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)
        data = json.loads(response.content)
        self.assertIn('average_paid', data)
        self.assertIn('technician_with_lowest_paid', data)
        self.assertIn('technician_with_highest_paid', data)
