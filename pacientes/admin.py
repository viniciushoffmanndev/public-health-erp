from django.contrib import admin
from .models import (
    UsuarioCadsus, Pessoa, Nacionalidade, TipoPessoa,
    Atividade, EstadoCivil, Escolaridade, LocalPermanencia,
    EtniaIndigena, ComunidadeTradicional, UsuarioCadsusMotivoCpf
)

# Base Mixin para evitar repetição de código nas tabelas Read-Only
class BaseReadOnlyAdmin(admin.ModelAdmin):
    def has_add_permission(self, request): return False
    def has_change_permission(self, request, obj=None): return False
    def has_delete_permission(self, request, obj=None): return False


@admin.register(UsuarioCadsus)
class UsuarioCadsusAdmin(admin.ModelAdmin):
    # Exibe dados capitais e limpos para triagem e busca na listagem
    list_display = ('cd_usu_cadsus', 'nm_usuario', 'cpf', 'dt_nascimento', 'prontuario', 'st_vivo')
    search_fields = ('nm_usuario', 'cpf', 'prontuario')
    list_filter = ('sg_sexo', 'st_vivo', 'st_excluido')
    ordering = ('cd_usu_cadsus',)

    # Transforma dropdowns em inputs de busca numéricos para poupar memória do servidor
    raw_id_fields = (
        'cod_cid_nascimento', 'cd_municipio_residencia', 'cd_cbo', 
        'cd_escolaridade', 'cd_usuario', 'cd_usuario_cad',
        'cd_pais_nascimento', 'cd_raca', 'cd_estado_civil',
        'empresa_responsavel', 'cd_local_permanencia', 'nr_atendimento_origem',
        'cd_endereco', 'cd_usu_cadsus_responsavel', 'cd_etnia',
        'cd_gerenciador_arquivo', 'cd_estabelecimento_cerest', 'cd_usu_cadsus_unificado',
        'cd_equipe', 'cd_equipe_profissional', 'cd_comunidade',
        'cd_motivo_cpf', 'cd_equipe_vinculo'
    )


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('cod_pessoa', 'descricao', 'cnpj_cpf', 'fis_jur', 'dt_cadastro')
    search_fields = ('descricao', 'cnpj_cpf')
    list_filter = ('fis_jur', 'cliente', 'fornecedor', 'funcionario')
    ordering = ('cod_pessoa',)
    
    # Protege a memória contra dropdowns pesados nas chaves estrangeiras
    raw_id_fields = ('cod_atv', 'cod_tip_pessoa', 'cod_representante')


# --- TABELAS DE REFERÊNCIA/DOMÍNIO BLINDADAS (READ-ONLY) ---

@admin.register(Nacionalidade)
class NacionalidadeAdmin(BaseReadOnlyAdmin):
    list_display = ('cd_pais', 'ds_pais', 'cd_pni', 'cd_esus')
    search_fields = ('ds_pais', 'cd_pais')
    ordering = ('ds_pais',)


@admin.register(TipoPessoa)
class TipoPessoaAdmin(BaseReadOnlyAdmin):
    list_display = ('cod_tip_pessoa', 'descricao', 'sigla', 'version')
    search_fields = ('descricao', 'sigla', 'cod_tip_pessoa')
    ordering = ('cod_tip_pessoa',)


@admin.register(Atividade)
class AtividadeAdmin(BaseReadOnlyAdmin):
    list_display = ('cod_atv', 'descricao', 'version')
    search_fields = ('descricao', 'cod_atv')
    ordering = ('descricao',)


@admin.register(EstadoCivil)
class EstadoCivilAdmin(BaseReadOnlyAdmin):
    list_display = ('cd_estado_civil', 'ds_estado_civil', 'version')
    search_fields = ('ds_estado_civil', 'cd_estado_civil')
    ordering = ('cd_estado_civil',)


@admin.register(Escolaridade)
class EscolaridadeAdmin(BaseReadOnlyAdmin):
    list_display = ('cd_escolaridade', 'ds_escolaridade', 'version')
    search_fields = ('ds_escolaridade', 'cd_escolaridade')
    ordering = ('cd_escolaridade',)


@admin.register(LocalPermanencia)
class LocalPermanenciaAdmin(BaseReadOnlyAdmin):
    list_display = ('cd_local_permanencia', 'ds_local_permanencia', 'version')
    search_fields = ('ds_local_permanencia', 'cd_local_permanencia')
    ordering = ('cd_local_permanencia',)


@admin.register(EtniaIndigena)
class EtniaIndigenaAdmin(BaseReadOnlyAdmin):
    list_display = ('cd_etnia', 'ds_etnia', 'cd_sus', 'version')
    search_fields = ('ds_etnia', 'cd_etnia', 'cd_sus')
    ordering = ('ds_etnia',)


@admin.register(ComunidadeTradicional)
class ComunidadeTradicionalAdmin(BaseReadOnlyAdmin):
    list_display = ('cd_comunidade', 'ds_comunidade', 'cd_sus', 'version')
    search_fields = ('ds_comunidade', 'cd_comunidade')
    ordering = ('ds_comunidade',)


@admin.register(UsuarioCadsusMotivoCpf)
class UsuarioCadsusMotivoCpfAdmin(BaseReadOnlyAdmin):
    list_display = ('cd_motivo_cpf', 'descricao', 'ativo', 'version')
    search_fields = ('descricao', 'cd_motivo_cpf')
    ordering = ('cd_motivo_cpf',)