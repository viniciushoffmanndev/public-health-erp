from rest_framework import serializers
from .models import Cidade, Estado

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = ['cod_est']  # Usando a PK real numérica do banco legado


class CidadeSerializer(serializers.ModelSerializer):
    # Retorna diretamente o código numérico do estado relacionado
    estado_id = serializers.IntegerField(source='cod_est.cod_est', read_only=True)

    class Meta:
        model = Cidade
        fields = [
            'cod_cid', 
            'descricao', 
            'estado_id', 
            'cd_esus', 
            'flag_liberar_disp'
        ]