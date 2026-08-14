from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PuertaViewSet, VueloViewSet

router = DefaultRouter()
router.register(r"puertas", PuertaViewSet, basename="puertas")
router.register(r"vuelos", VueloViewSet, basename="vuelos")

urlpatterns = []
urlpatterns += router.urls