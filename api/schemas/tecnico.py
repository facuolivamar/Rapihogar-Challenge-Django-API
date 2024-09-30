from rest_framework import serializers
from rapihogar.models import Tecnico
from api.services.tecnico import TecnicoService


class TecnicoSerializer(serializers.ModelSerializer):
    """
    Serializer class for serializing individual technician (`Tecnico`) data, 
    including calculated fields like total payment, hours worked, and the number of service requests (`pedidos`).
    """
    full_name = serializers.SerializerMethodField()
    total_paid = serializers.SerializerMethodField(read_only=True)
    hours_worked = serializers.SerializerMethodField(read_only=True)
    pedidos_count = serializers.SerializerMethodField(read_only=True)

    def __init__(self, *args, **kwargs):
        """
        Override the constructor to initialize a TecnicoService for each technician instance.
        This allows us to reuse the service layer logic to calculate fields like total payment and hours worked.
        """
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
    """
    Serializer class for serializing technician report data.
    This includes the technician's total payment, hours worked, and number of service requests (`pedidos`).
    Unlike TecnicoSerializer, this one works with already calculated values,
    hence it uses simple fields for `total_paid`, `hours_worked`, and `pedidos_count`.
    """
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
    """
    Serializer class for generating reports across multiple technicians.
    This includes average payment, the list of technicians earning below average,
    and the technicians with the lowest and highest payments.
    """
    average_paid = serializers.FloatField()
    technicians_below_average = TecnicoReportSerializer(many=True)
    technician_with_lowest_paid = TecnicoReportSerializer()
    technician_with_highest_paid = TecnicoReportSerializer()
