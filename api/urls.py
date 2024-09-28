from rest_framework import routers
from django.urls import path
from .resources.company import CompanyViewSet
from .resources.pedido import PedidoUpdateView
from .resources.tecnico import TecnicoListView, TecnicoReportView

router = routers.DefaultRouter()
router.register(r'company', CompanyViewSet, basename='company')


urlpatterns = router.urls + [
    path(
        "pedido/<int:pk>",
        PedidoUpdateView.as_view(),
        name="pedido",
    ),
    path(
        "tecnico/",
        TecnicoListView.as_view(),
        name="tecnico",
    ),
    path(
        "tecnico/informe",
        TecnicoReportView.as_view(),
        name="tecnico/informe",
    ),
]
