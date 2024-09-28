from rest_framework import viewsets
from rapihogar.models import Company, Pedido
from rest_framework import generics
from api.serializers import CompanySerializer, PedidoSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.filter()


class PedidoUpdateView(generics.UpdateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
