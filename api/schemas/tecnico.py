from rest_framework import serializers
from rapihogar.models import Tecnico
from api.services.tecnico import TecnicoService


class TecnicoSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    total_paid = serializers.SerializerMethodField(read_only=True)
    hours_worked = serializers.SerializerMethodField(read_only=True)
    pedidos_count = serializers.SerializerMethodField(read_only=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:
            self.services = {
                tecnico.id: TecnicoService(tecnico) for tecnico in self.instance
            }

    def get_full_name(self, obj):
        return obj.full_name

    def get_total_paid(self, obj):
        return self.services[obj.id].get_total_paid()

    def get_hours_worked(self, obj):
        return self.services[obj.id].get_hours_worked()

    def get_pedidos_count(self, obj):
        return self.services[obj.id].get_pedidos_count()

    class Meta:
        model = Tecnico
        fields = ['id', 'full_name', 'total_paid', 'hours_worked', 'pedidos_count']


class TecnicoReportSerializer(serializers.ModelSerializer):
    total_paid = serializers.FloatField()
    hours_worked = serializers.FloatField()
    pedidos_count = serializers.IntegerField()

    def get_total_paid(self, obj):
        return obj.get_total_paid()

    def get_hours_worked(self, obj):
        return obj.get_hours_worked()

    def get_pedidos_count(self, obj):
        return obj.get_pedidos_count()

    class Meta:
        model = Tecnico
        fields = ['id', 'full_name', 'total_paid', 'hours_worked', 'pedidos_count']


class ReportSerializer(serializers.Serializer):
    average_paid = serializers.FloatField()
    technicians_below_average = TecnicoReportSerializer(many=True)
    technician_with_lowest_paid = TecnicoReportSerializer()
    technician_with_highest_paid = TecnicoReportSerializer()
