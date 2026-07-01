from rest_framework import serializers
from .models import Cidade, Estado

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = ['public_id']  # Usando o public_id (UUIDv7) que está mapeado no seu modelo


class CidadeSerializer(serializers.ModelSerializer):
    # Retorna o UUID público do estado em vez do código interno do banco
    estado_id = serializers.UUIDField(source='cod_est.public_id', read_only=True)

    class Meta:
        model = Cidade
        fields = [
            'cod_cid', 
            'public_id', 
            'descricao', 
            'estado_id', 
            'cd_esus', 
            'flag_liberar_disp'
        ]