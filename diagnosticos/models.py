from django.db import models
import uuid6


class CidClassificacao(models.Model):
    class Meta:
        managed = False
        db_table = 'cid_classificacao'
    
    def __str__(self):
        return f"Classificação CID {self.pk}"


class Cid(models.Model):
    cd_cid = models.CharField(primary_key=True, max_length=8)
    public_id = models.UUIDField(default=uuid6.uuid7, editable=False, unique=True, db_index=True, db_column='uuid_publico')
    nm_cid = models.CharField()
    tp_agravo = models.SmallIntegerField(db_comment='0 - Sem Agravo\n1 - Agravo de notificação\n2 - Agravo de bloqueio')
    tp_sexo = models.CharField(max_length=1, db_comment='M - Masculino\nF - Feminino\nI - Indiferente/Ambos')
    version = models.BigIntegerField()
    cd_classificacao = models.ForeignKey('CidClassificacao', models.DO_NOTHING, db_column='cd_classificacao', blank=True, null=True)
    flag_cid_categoria = models.CharField(max_length=1)
    ativo = models.SmallIntegerField(blank=True, null=True)
    flag_registro_diarreia = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cid'
        db_table_comment = 'Cadastro internacional de doenças'

    def __str__(self):
        return f"{self.cd_cid} - {self.nm_cid}"


class Ciap(models.Model):
    cd_ciap = models.BigIntegerField(primary_key=True)
    public_id = models.UUIDField(default=uuid6.uuid7, editable=False, unique=True, db_index=True, db_column='uuid_publico')
    referencia = models.CharField()
    componente = models.SmallIntegerField()
    capitulo = models.CharField()
    titulo_original = models.CharField()
    titulo_leigo = models.CharField()
    cd_cid_mais_frequente = models.ForeignKey(Cid, models.DO_NOTHING, db_column='cd_cid_mais_frequente', blank=True, null=True)
    definicao = models.CharField(blank=True, null=True)
    criterios_inclusao = models.CharField(blank=True, null=True)
    criterios_exclusao = models.CharField(blank=True, null=True)
    considerar = models.CharField(blank=True, null=True)
    nota = models.CharField(blank=True, null=True)
    version = models.BigIntegerField()
    situacao = models.SmallIntegerField()
    cd_esus = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ciap'

    def __str__(self):
        return f"CIAP {self.referencia} - {self.titulo_original}"