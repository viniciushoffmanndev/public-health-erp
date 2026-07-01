from django.contrib import admin
from .models import Cidade, Estado, EnderecoUsuarioCadsus, EndEstruturadoDistrito

@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'get_db_table')  # Mudamos de 'db_table' para o método personalizado

    @admin.display(description='Tabela Física')
    def get_db_table(self, obj):
        return obj._meta.db_table


@admin.register(EndEstruturadoDistrito)
class EndEstruturadoDistritoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'get_db_table')  # Mudamos de 'db_table' para o método personalizado

    @admin.display(description='Tabela Física')
    def get_db_table(self, obj):
        return obj._meta.db_table


@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ('cod_cid', 'descricao', 'cod_est', 'cd_esus')
    list_filter = ('cod_est',)
    search_fields = ('descricao', 'cod_cid', 'cd_esus')
    ordering = ('descricao',)


@admin.register(EnderecoUsuarioCadsus)
class EnderecoUsuarioCadsusAdmin(admin.ModelAdmin):
    list_display = ('cd_endereco', 'nm_logradouro', 'nr_logradouro', 'nm_bairro', 'cod_cid')
    list_filter = ('cod_cid__cod_est', 'st_ativo')
    search_fields = ('nm_logradouro', 'nm_bairro', 'cep', 'cd_endereco')
    raw_id_fields = ('cod_cid', 'empresa', 'cd_endereco_estruturado')