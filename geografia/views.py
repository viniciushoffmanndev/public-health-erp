
# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Cidade
from .serializers import CidadeSerializer

class CidadeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint que permite visualizar as cidades cadastradas no ERP.
    """
    queryset = Cidade.objects.select_related('cod_est').all().order_by('descricao')
    serializer_class = CidadeSerializer
    permission_classes = [IsAuthenticated]  # Protege o endpoint pedindo autenticação