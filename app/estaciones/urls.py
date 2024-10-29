from django.urls import path
from .views import EstacionListCreateAPIView, EstacionCercanaAPIView

urlpatterns = [
    path('estaciones/', EstacionListCreateAPIView.as_view(), name='estacion-list'),  # Para listar y crear estaciones
    path('estaciones/cercana/<int:id>/', EstacionCercanaAPIView.as_view(), name='estacion-cercana'),  # Para la estación más cercana
]
