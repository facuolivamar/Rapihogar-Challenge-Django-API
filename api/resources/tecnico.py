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
    """
    Custom filter class to enable filtering of `Tecnico` objects based on their first and last names.
    Define filters for first name and last name with case-insensitive containment.
    """
    first_name = filters.CharFilter(field_name="first_name", lookup_expr="icontains")
    last_name = filters.CharFilter(field_name="last_name", lookup_expr="icontains")

    class Meta:
        model = Tecnico
        fields = ["first_name", "last_name"]


class TecnicoListView(generics.ListAPIView):
    """
    API view for listing all `Tecnico` instances with support for filtering and ordering.
    Inherits from Django REST Framework's ListAPIView to provide GET requests for the list of technicians.
    """
    queryset = Tecnico.objects.all()
    serializer_class = TecnicoSerializer
    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
    ]
    filterset_class = TecnicoFilter


class TecnicoReportView(APIView):
    """
    API view for generating a report on all technicians, including average payment and other statistics.
    Inherits from Django REST Framework's APIView to provide more flexibility in handling requests.
    """
    def get(self, request):
        """
        Handle GET requests to retrieve the report data for technicians.
        """
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
