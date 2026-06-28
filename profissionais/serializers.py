from rest_framework import serializers
from .models import Profissional

class ProfissionalMinimoSerializer(serializers.ModelSerializer):
    # NOTA: Se a coluna de nome no seu banco legado for diferente de 'nm_profissional'
    # (ex: 'descricao' ou 'nome'), ajuste o parâmetro source abaixo!
    nome = serializers.CharField(source='nm_profissional', default='Profissional Cadastrado')

    class Meta:
        model = Profissional
        fields = ['cd_profissional', 'nome']