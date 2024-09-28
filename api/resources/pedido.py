from rapihogar.models import Pedido
from api.schemas.pedido import PedidoSerializer
from rest_framework import generics


class PedidoUpdateView(generics.UpdateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
