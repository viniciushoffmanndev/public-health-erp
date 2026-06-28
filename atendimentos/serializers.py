from rest_framework import serializers
from .models import Atendimento
from pacientes.serializers import PacienteMinimoSerializer
from profissionais.serializers import ProfissionalMinimoSerializer
import uuid6

class AtendimentoSerializer(serializers.ModelSerializer):
    uuid_v7 = serializers.SerializerMethodField()
    id_interno = serializers.IntegerField(source='nr_atendimento')
    data_atendimento = serializers.DateTimeField(source='dt_atendimento', format='%d/%m/%Y %H:%M', allow_null=True)

    # --- ENGENHARIA DE MERCADO: NESTED SERIALIZERS ---
    # O DRF vai ler o relacionamento ForeignKey do Django e aplicar os sub-serializers automaticamente
    paciente = PacienteMinimoSerializer(source='cd_usu_cadsus', read_only=True)
    profissional = ProfissionalMinimoSerializer(source='cd_profissional', read_only=True)

    class Meta:
        model = Atendimento
        fields = [
            'id_interno',
            'uuid_v7',
            'data_atendimento',
            'status',
            'paciente',     # Substitui o antigo id_paciente bruto por um objeto rico
            'profissional'  # Substitui o antigo id_profissional bruto por um objeto rico
        ]

    def get_uuid_v7(self, obj):
        return str(uuid6.uuid7())