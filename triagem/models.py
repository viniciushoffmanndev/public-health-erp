from django.db import models
import uuid6


class ClassificacaoRisco(models.Model):
    cd_classificacao_risco = models.BigIntegerField(primary_key=True)
    public_id = models.UUIDField(default=uuid6.uuid7, editable=False, unique=True, db_index=True, db_column='uuid_publico')
    nivel_gravidade = models.SmallIntegerField(unique=True)
    descricao = models.CharField(max_length=50)
    tempo_maximo = models.IntegerField(blank=True, null=True)
    version = models.BigIntegerField()
    ativo = models.SmallIntegerField(blank=True, null=True)
    flag_ativar_cr = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'classificacao_risco'

    def __str__(self):
        return f"Nível {self.nivel_gravidade} - {self.descricao}"


class MotivosCancelamento(models.Model):
    cod_motivo = models.IntegerField(primary_key=True)
    public_id = models.UUIDField(default=uuid6.uuid7, editable=False, unique=True, db_index=True, db_column='uuid_publico')
    descricao = models.CharField(max_length=40)
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'motivos_cancelamento'
        db_table_comment = 'Tabela de motivos de cancelamentos'

    def __str__(self):
        return self.descricao