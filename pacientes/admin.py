# Register your models here.
from django.contrib import admin
from .models import UsuarioCadsus, Pessoa, Nacionalidade, TipoPessoa

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


@admin.register(Nacionalidade)
class NacionalidadeAdmin(admin.ModelAdmin):
    list_display = ('cd_pais', 'ds_pais', 'cd_pni', 'cd_esus')
    search_fields = ('ds_pais', 'cd_pais')
    ordering = ('ds_pais',)

    def has_add_permission(self, request): return False
    def has_change_permission(self, request, obj=None): return False
    def has_delete_permission(self, request, obj=None): return False

@admin.register(TipoPessoa)
class TipoPessoaAdmin(admin.ModelAdmin):
    list_display = ('cod_tip_pessoa', 'descricao', 'sigla', 'version')
    search_fields = ('descricao', 'sigla', 'cod_tip_pessoa')
    ordering = ('cod_tip_pessoa',)

    # Blindagem para tabelas de referência estática
    def has_add_permission(self, request): return False
    def has_change_permission(self, request, obj=None): return False
    def has_delete_permission(self, request, obj=None): return False