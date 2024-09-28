import json
from rapihogar.models import User
from django.urls import reverse

from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rapihogar.models import Company, Tecnico, Pedido


class CompanyListCreateAPIViewTestCase(APITestCase):
    url = reverse("company-list")

    def setUp(self):
        self.username = "user_test"
        self.email = "test@rapihigar.com"
        self.password = "Rapi123"
        self.user = User.objects.create_user(self.username, self.email, self.password)
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_create_company(self):
        response = self.client.post(self.url,
                                    {
                                        "name": "company delete!",
                                        "phone": "123456789",
                                        "email": "test@rapihigar.com",
                                        "website": "http://www.rapitest.com"
                                    }
                                    )
        self.assertEqual(201, response.status_code)

    def test_list_company(self):
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)
        self.assertTrue(len(json.loads(response.content)) == Company.objects.count())

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



class PedidoUpdateAPIViewTestCase(APITestCase):
    url = reverse("pedido", args=[1])

    def setUp(self):
        # Crear usuario de prueba y autenticación
        self.username = "user_test"
        self.email = "test@rapihogar.com"
        self.password = "Rapi123"
        self.user = User.objects.create_user(self.username, self.email, self.password, first_name="Test", last_name="User")
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

        # Crear técnico y pedido de prueba
        self.tecnico = Tecnico.objects.create(first_name="Pedro", last_name="Garcia")
        self.pedido = Pedido.objects.create(client=self.user, technician=self.tecnico, type_request=Pedido.PEDIDO, hours_worked=5)

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_update_pedido(self):
        data = {
            "type_request": 0,
            "hours_worked": 10
        }
        response = self.client.patch(self.url, data)
        self.assertEqual(200, response.status_code)
        self.pedido.refresh_from_db()
        self.assertEqual(self.pedido.type_request, 0)
        self.assertEqual(self.pedido.hours_worked, 10)



