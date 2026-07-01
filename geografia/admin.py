from django.contrib import admin
from .models import Cidade, Estado, EnderecoUsuarioCadsus, EndEstruturadoDistrito

@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    # Exibe a PK real numérica encontrada no information_schema
    list_display = ('cod_est', 'get_db_table')

    @admin.display(description='Tabela Física')
    def get_db_table(self, obj):
        return obj._meta.db_table


@admin.register(EndEstruturadoDistrito)
class EndEstruturadoDistritoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'get_db_table')

    @admin.display(description='Tabela Física')
    def get_db_table(self, obj):
        return obj._meta.db_table


@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    # Listagem limpa e ultra performática usando campos reais
    list_display = ('cod_cid', 'descricao', 'cod_est', 'cd_esus')
    list_filter = ('cod_est',)
    search_fields = ('descricao', 'cod_cid', 'cd_esus')
    ordering = ('descricao',)


@admin.register(EnderecoUsuarioCadsus)
class EnderecoUsuarioCadsusAdmin(admin.ModelAdmin):
    list_display = ('cd_endereco', 'nm_logradouro', 'nr_logradouro', 'nm_bairro', 'cod_cid')
    list_filter = ('st_ativo',)  # Removemos o filtro aninhado cod_cid__cod_est caso o relacionamento estivesse instável
    search_fields = ('nm_logradouro', 'nm_bairro', 'cep', 'cd_endereco')
    raw_id_fields = ('cod_cid',) # Evita dropdowns pesados que travam o admin carregando tabelas gigantes legadas