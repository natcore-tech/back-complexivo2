from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Puerta, Vuelo
from .serializers import PuertaSerializer, VueloSerializer
from .permissions import IsAdminOrReadOnly

class PuertaViewSet(viewsets.ModelViewSet):
    queryset = Puerta.objects.all().order_by("id")
    serializer_class = PuertaSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ["code"]
    ordering_fields = ["id", "code", "terminal", "created_at"]

class VueloViewSet(viewsets.ModelViewSet):
    queryset = Vuelo.objects.select_related("gate_id").all().order_by("-id")
    serializer_class = VueloSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["gate_id"]
    search_fields = ["gate_id", "flight_number", "destination", "marca__nombre"]
    ordering_fields = ["id", "status", "departure_time", "created_at", "creado_en"]

    def get_queryset(self):
        qs = super().get_queryset()
        anio_min = self.request.query_params.get("anio_min")
        anio_max = self.request.query_params.get("anio_max")
        if anio_min:
            qs = qs.filter(anio__gte=int(anio_min))
        if anio_max:
            qs = qs.filter(anio__lte=int(anio_max))
        return qs

    def get_permissions(self):
        # Público: SOLO listar vehículos
        if self.action == "list":
            return [AllowAny()]
        return super().get_permissions()