from django.contrib import admin
from .models import (Profissional, TabelaCbo, Usuarios, OrgaoEmissor, TabelaSubgrupoCbo, TabelaCboGrupoAtendimento, ProgramaWeb)

@admin.register(Profissional)
class ProfissionalAdmin(admin.ModelAdmin):
    list_display = ('cd_profissional', 'nm_profissional', 'cpf', 'cd_cns', 'nr_registro', 'ativo')
    list_filter = ('ativo', 'sexo')
    search_fields = ('nm_profissional', 'cpf', 'cd_cns', 'nr_registro', 'cd_profissional')
    ordering = ('nm_profissional',)
    raw_id_fields = ('cod_cid', 'cd_tipo_logradouro', 'cod_cid_nasc', 'cd_usuario', 'cd_tipo_prestador_ipe', 'cd_cnes_processo')

@admin.register(TabelaCbo)
class TabelaCboAdmin(admin.ModelAdmin):
    list_display = ('cd_cbo', 'ds_cbo', 'cd_grupo_cbo', 'cd_subgrupo_cbo', 'ativo')
    search_fields = ('cd_cbo', 'ds_cbo')
    list_filter = ('ativo', 'tipo_profissional_saude')
    ordering = ('cd_cbo',)
    
    # Remove os links de clique para evitar o disparo do bug de relacionamento composto
    list_display_links = None 

    # Desativa operações de escrita
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(Usuarios)
class UsuariosAdmin(admin.ModelAdmin):
    list_display = ('cd_usuario', 'ds_login', 'nm_usuario', 'ds_status', 'dt_ult_acesso')
    list_filter = ('ds_status', 'ds_nivel')
    search_fields = ('ds_login', 'nm_usuario', 'cpf')
    ordering = ('ds_login',)
    raw_id_fields = ('cd_modulo', 'empresa_padrao', 'cd_profissional', 'cod_centro_custo', 'cd_usuario_cad', 'cd_certificado_digital', 'cd_prg_web')

@admin.register(OrgaoEmissor)
class OrgaoEmissorAdmin(admin.ModelAdmin):
    list_display = ('cd_orgao_emissor', 'sg_orgao_emissor', 'ds_orgao_emissor', 'fl_saude', 'get_db_table')
    search_fields = ('sg_orgao_emissor', 'ds_orgao_emissor', 'cd_orgao_emissor')
    ordering = ('sg_orgao_emissor',)
    
    @admin.display(description='Tabela Física')
    def get_db_table(self, obj): 
        return obj._meta.db_table

@admin.register(TabelaSubgrupoCbo)
class TabelaSubgrupoCboAdmin(admin.ModelAdmin):
    list_display = ('cd_grupo_cbo', 'cd_subgrupo_cbo', 'ds_subgrupo_cbo', 'version')
    search_fields = ('ds_subgrupo_cbo',)
    ordering = ('cd_grupo_cbo', 'cd_subgrupo_cbo')
    list_display_links = None  # Remove os links de clique na listagem

    # 1. Bloqueia a permissão de alteração (evita a rota /change/)
    def has_change_permission(self, request, obj=None):
        return False

    # 2. Bloqueia a permissão de adição (remove o botão "+ Add")
    def has_add_permission(self, request):
        return False

    # 3. Bloqueia a permissão de exclusão
    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(TabelaCboGrupoAtendimento)
class TabelaCboGrupoAtendimentoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'get_db_table')
    def get_db_table(self, obj): return obj._meta.db_table

@admin.register(ProgramaWeb)
class ProgramaWebAdmin(admin.ModelAdmin):
    list_display = ('cd_prg_web', 'ds_prg_web', 'ativo', 'get_db_table')
    search_fields = ('ds_prg_web', 'cd_prg_web')
    list_filter = ('ativo',)
    ordering = ('ds_prg_web',)

    @admin.display(description='Tabela Física')
    def get_db_table(self, obj):
        return obj._meta.db_table