from rapihogar.models import Company
from rest_framework import routers
from django.urls import path, include
from .views import CompanyViewSet, TecnicoListView, PedidoUpdateView

router = routers.DefaultRouter()
router.register(r'company', CompanyViewSet, basename='company')


urlpatterns = router.urls + [
    path(
        "tecnico/",
        TecnicoListView.as_view(),
        name="tecnico",
    ),
    path(
        "pedido/<int:pk>",
        PedidoUpdateView.as_view(),
        name="pedido",
    ),
]
