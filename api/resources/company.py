from rest_framework import viewsets
from rapihogar.models import Company
from api.schemas.company import CompanySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.filter()
