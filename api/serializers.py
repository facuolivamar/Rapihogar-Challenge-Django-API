from rest_framework import serializers
from rapihogar.models import Company, Pedido

class CompanySerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Company
        fields = '__all__'


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'
