from django.contrib import admin
from .models import CidClassificacao, Cid, Ciap

class BaseReadOnlyAdmin(admin.ModelAdmin):
    """Garante que dados mestres do SUS não sejam alterados acidentalmente via Admin."""
    def has_add_permission(self, request): return False
    def has_change_permission(self, request, obj=None): return False
    def has_delete_permission(self, request, obj=None): return False


@admin.register(CidClassificacao)
class CidClassificacaoAdmin(BaseReadOnlyAdmin):
    list_display = ('cd_classificacao', 'descricao', 'prazo_encerramento', 'version')
    search_fields = ('cd_classificacao', 'descricao')
    ordering = ('cd_classificacao',)


@admin.register(Cid)
class CidAdmin(BaseReadOnlyAdmin):
    # Usamos uma função auxiliar para encurtar o nome do CID na listagem
    list_display = ('cd_cid', 'nome_curto', 'tp_agravo', 'tp_sexo', 'ativo')
    search_fields = ('cd_cid', 'nm_cid')
    list_filter = ('tp_agravo', 'tp_sexo', 'ativo')
    ordering = ('cd_cid',)
    
    # Evita travar a memória ao carregar chaves estrangeiras
    raw_id_fields = ('cd_classificacao',)

    def nome_curto(self, obj):
        return obj.nm_cid[:60] + '...' if len(obj.nm_cid) > 60 else obj.nm_cid
    nome_curto.short_description = 'Nome da Doença (CID)'


@admin.register(Ciap)
class CiapAdmin(BaseReadOnlyAdmin):
    list_display = ('cd_ciap', 'referencia', 'capitulo', 'titulo_curto', 'situacao')
    search_fields = ('cd_ciap', 'referencia', 'titulo_original', 'titulo_leigo')
    list_filter = ('componente', 'situacao')
    ordering = ('referencia',)
    
    # Amarra perfeita com o código textual do CID usando lupa de busca performática
    raw_id_fields = ('cd_cid_mais_frequente',)

    def titulo_curto(self, obj):
        return obj.titulo_original[:60] + '...' if len(obj.titulo_original) > 60 else obj.titulo_original
    titulo_curto.short_description = 'Título Original'