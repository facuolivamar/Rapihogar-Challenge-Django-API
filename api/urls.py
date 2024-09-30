from rest_framework import routers
from django.urls import path
from .resources.company import CompanyViewSet
from .resources.pedido import PedidoUpdateView
from .resources.tecnico import TecnicoListView, TecnicoReportView

router = routers.DefaultRouter()
# Register the CompanyViewSet with the router, allowing RESTful operations on company resources
router.register(r'company', CompanyViewSet, basename='company')


# Define the urlpatterns to include both router-generated URLs and custom paths.
urlpatterns = router.urls + [
    # URL pattern for updating a specific pedido by its primary key (pk). Patch operations are allowed.
    path(
        "pedido/<int:pk>",
        PedidoUpdateView.as_view(),
        name="pedido",
    ),
    # URL pattern for listing all technicians. A single technician can be returned by providing its ID.
    path(
        "tecnico/",
        TecnicoListView.as_view(),
        name="tecnico",
    ),
    # URL pattern for generating a report on technicians.
    path(
        "tecnico/informe",
        TecnicoReportView.as_view(),
        name="tecnico/informe",
    ),
]
