from django.urls import path
from .views import AtendimentoListAPIView

urlpatterns = [
    path('api/v1/recentes/', AtendimentoListAPIView.as_view(), name='atendimentos_recentes_api'),
]