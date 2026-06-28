from rest_framework.generics import ListAPIView
from .models import Atendimento
from .serializers import AtendimentoSerializer

class AtendimentoListAPIView(ListAPIView):
    """
    Endpoint de alta performance que realiza a junção das ilhas de dados
    em uma única query SQL otimizada.
    """
    serializer_class = AtendimentoSerializer

    def get_queryset(self):
        # O select_related força o Django a fazer um JOIN no banco de dados (Neon DB).
        # Ele traz os dados do Atendimento, Paciente e Médico de UMA SÓ VEZ.
        return Atendimento.objects.select_related(
            'cd_usu_cadsus', 
            'cd_profissional'
        ).order_by('-dt_atendimento')[:10]