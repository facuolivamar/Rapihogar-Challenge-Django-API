import json
from rapihogar.models import User
from django.urls import reverse

from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rapihogar.models import Tecnico, Pedido


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

