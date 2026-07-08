from django.contrib import admin
from .models import Procedimento, ProcedimentoFinanciamento

class BaseReadOnlyAdmin(admin.ModelAdmin):
    """Garante que tabelas de catálogo ou parâmetros do SUS não sejam alteradas por engano."""
    def has_add_permission(self, request): return False
    def has_change_permission(self, request, obj=None): return False
    def has_delete_permission(self, request, obj=None): return False


@admin.register(Procedimento)
class ProcedimentoAdmin(admin.ModelAdmin):
    # Exibe informações vitais do procedimento na listagem
    list_display = ('exibir_codigo', 'ds_procedimento', 'situacao', 'faturavel', 'flag_consulta_esus')
    
    # Mecanismo de busca rápida indexada (código ou termo do procedimento)
    search_fields = ('cd_procedimento', 'ds_procedimento')
    
    # Filtros laterais para auditoria rápida do faturamento
    list_filter = ('situacao', 'faturavel', 'flag_consulta_esus')
    
    # Ordenação lógica sequencial pelo código SUS
    ordering = ('cd_procedimento',)

    # JOGADA: A tabela SIGTAP é gigante. Usamos raw_id_fields para as FKs 
    # não tentarem carregar milhares de registros em dropdowns e estourarem a memória.
    raw_id_fields = ('empresa_bpa', 'cd_profissional_bpa', 'cd_tp_tabela')

    @admin.display(description='Código SUS')
    def exibir_codigo(self, obj):
        return f"{int(obj.cd_procedimento)}"


@admin.register(ProcedimentoFinanciamento)
class ProcedimentoFinanciamentoAdmin(BaseReadOnlyAdmin):
    # Tabelas de domínio/referência estáveis entram como Read-Only
    list_display = ('cd_financiamento', 'ds_financiamento', 'dt_competencia')
    search_fields = ('ds_financiamento', 'cd_financiamento')
    list_filter = ('dt_competencia',)
    ordering = ('cd_financiamento',)
