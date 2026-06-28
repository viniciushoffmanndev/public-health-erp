from rest_framework import serializers
from .models import UsuarioCadsus

class PacienteMinimoSerializer(serializers.ModelSerializer):
    # Mapeamos o campo legível da nossa ilha
    nome = serializers.CharField(source='nm_usuario')
    cpf_mascarado = serializers.SerializerMethodField()

    class Meta:
        model = UsuarioCadsus
        fields = ['nome', 'cpf', 'cpf_mascarado']

    def get_cpf_mascarado(self, obj):
        # Mascaramento em tempo de execução para conformidade com a LGPD
        if obj.cpf and len(obj.cpf) >= 11:
            return f"***.{obj.cpf[3:6]}.{obj.cpf[6:9]}-**"
        return None