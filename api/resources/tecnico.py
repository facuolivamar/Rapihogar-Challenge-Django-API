from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from rest_framework.views import APIView

from rapihogar.models import Tecnico
from api.schemas.tecnico import TecnicoSerializer, ReportSerializer
from api.services.tecnico import ReportService


class TecnicoFilter(filters.FilterSet):
    first_name = filters.CharFilter(field_name="first_name", lookup_expr="icontains")
    last_name = filters.CharFilter(field_name="last_name", lookup_expr="icontains")

    class Meta:
        model = Tecnico
        fields = ["first_name", "last_name"]


class TecnicoListView(generics.ListAPIView):
    queryset = Tecnico.objects.all()
    serializer_class = TecnicoSerializer
    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
    ]
    filterset_class = TecnicoFilter


class TecnicoReportView(APIView):
    def get(self, request):
        tecnicos = Tecnico.objects.all()
        report_service = ReportService(tecnicos)

        data = {
            'average_paid': report_service.get_average_paid(),
            'technicians_below_average': [
                tecnico for tecnico in report_service.get_technicians_below_average()
            ],
            'technician_with_lowest_paid': report_service.get_technician_with_lowest_paid(),
            'technician_with_highest_paid': report_service.get_technician_with_highest_paid(),
        }

        serializer = ReportSerializer(data)
        return Response(serializer.data)
