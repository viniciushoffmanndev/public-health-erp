from django.contrib import admin
from .models import (
    Atendimento, AcaoProgramaticaGrupo, ClassificacaoAtendimento,
    Conduta, NaturezaProcuraTpAtendimento, LeitoQuarto, AtividadeGrupo
)

# Base Mixin para blindar as tabelas de domínio/referência estáveis
class BaseReadOnlyAdmin(admin.ModelAdmin):
    def has_add_permission(self, request): return False
    def has_change_permission(self, request, obj=None): return False
    def has_delete_permission(self, request, obj=None): return False


@admin.register(Atendimento)
class AtendimentoAdmin(admin.ModelAdmin):
    # Exibe os dados vitais do prontuário/atendimento na listagem geral
    list_display = (
        'nr_atendimento', 'nm_paciente', 'cd_profissional', 
        'dt_atendimento', 'status', 'tp_demanda', 'prioridade'
    )
    
    # Mecanismo de busca rápida indexada
    search_fields = ('nr_atendimento', 'nm_paciente', 'cpf', 'cns')
    
    # Filtros laterais performáticos para a gestão auditar os gargalos
    list_filter = ('status', 'tp_demanda', 'prioridade', 'dt_atendimento')
    
    # Ordenação padrão pelo atendimento mais recente
    ordering = ('-dt_atendimento',)

    # Transforma TODAS as ForeignKeys em inputs numéricos com lupa de busca.
    # Isso impede o Django de tentar dar um "SELECT ALL" em tabelas de 100k+ registros para montar dropdowns.
    raw_id_fields = (
        'empresa', 'cd_usu_cadsus', 'cod_motivo', 'cd_usuario_can', 
        'nr_prox_atendimento', 'cd_procedimento', 'cd_acao_programatica', 
        'cd_profissional', 'cd_usuario', 'nr_atendimento_origem', 
        'cd_cbo', 'cd_profissional_responsavel', 'cd_cid_principal', 
        'cd_cid_secundario', 'cd_cla_atendimento', 'cd_conduta', 
        'cd_domicilio', 'cd_endereco', 'nr_atendimento_principal', 
        'cd_leito', 'cd_convenio', 'cd_usu_cadsus_responsavel', 
        'classificacao_risco', 'cd_procedimento_atendimento', 'empresa_bpa', 
        'empresa_solicitante', 'cd_usuario_atendendo', 'cd_ciap', 
        'cd_atv_grupo', 'cd_profissional_auxiliar', 'cd_cbo_auxiliar', 
        'cd_profissional_chamada', 'cd_estabelecimento_cerest', 'cd_equipe'
    )


@admin.register(LeitoQuarto)
class LeitoQuartoAdmin(admin.ModelAdmin):
    list_display = ('cd_leito', 'ds_leito', 'situacao', 'dt_cadastro')
    search_fields = ('ds_leito', 'cd_leito')
    list_filter = ('situacao', 'sexo', 'tipo_leito')
    ordering = ('ds_leito',)
    
    # Evita carregar usuários e pacientes em dropdowns pesados
    raw_id_fields = ('nr_atendimento', 'cd_usuario_cad', 'cd_usuario_exc', 'cd_usu_cadsus')


@admin.register(AtividadeGrupo)
class AtividadeGrupoAdmin(admin.ModelAdmin):
    list_display = ('cd_atv_grupo', 'assunto', 'data_hora_inicio', 'situacao', 'qtd_participantes')
    search_fields = ('assunto', 'cd_atv_grupo')
    list_filter = ('situacao', 'turno', 'flag_origem')
    ordering = ('-data_hora_inicio',)
    
    raw_id_fields = ('empresa', 'cd_usu_baixa', 'cd_empresa_bpa')


# --- TABELAS AUXILIARES E PIVOTS REGISTRADAS COMO READ-ONLY ---

@admin.register(AcaoProgramaticaGrupo)
class AcaoProgramaticaGrupoAdmin(BaseReadOnlyAdmin):
    list_display = ('cd_acao_programatica', 'cd_grupo_atendimento', 'version')
    ordering = ('cd_acao_programatica',)


@admin.register(ClassificacaoAtendimento)
class ClassificacaoAtendimentoAdmin(BaseReadOnlyAdmin):
    list_display = ('cd_cla_atendimento', 'ds_cla_atendimento', 'ordem', 'situacao')
    search_fields = ('ds_cla_atendimento', 'cd_cla_atendimento')
    ordering = ('ordem',)


@admin.register(Conduta)
class CondutaAdmin(BaseReadOnlyAdmin):
    list_display = ('cd_conduta', 'ds_conduta', 'flag_retorno', 'tp_conduta')
    search_fields = ('ds_conduta', 'cd_conduta')
    ordering = ('cd_conduta',)


@admin.register(NaturezaProcuraTpAtendimento)
class NaturezaProcuraTpAtendimentoAdmin(BaseReadOnlyAdmin):
    list_display = ('cd_nat_proc_tp_atendimento', 'cd_nat_procura', 'cd_tp_atendimento', 'visivel')
    ordering = ('cd_nat_proc_tp_atendimento',)