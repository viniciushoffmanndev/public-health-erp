from django.db import models

class CidClassificacao(models.Model):
    cd_classificacao = models.BigIntegerField(primary_key=True, db_column='cd_classificacao')
    descricao = models.CharField(max_length=150, blank=True, null=True, db_column='descricao')
    version = models.BigIntegerField(db_column='version')
    flag_notificacao_concomitante = models.SmallIntegerField(blank=True, null=True, db_column='flag_notificacao_concomitante')
    cd_cid_agrupador = models.ForeignKey('Cid', models.DO_NOTHING, db_column='cd_cid_agrupador', blank=True, null=True)
    prazo_encerramento = models.IntegerField(blank=True, null=True, db_column='prazo_encerramento')
    cd_ficha_investigacao_agravo = models.BigIntegerField(blank=True, null=True, db_column='cd_ficha_investigacao_agravo')

    class Meta:
        managed = False
        db_table = 'cid_classificacao'
        verbose_name = 'Classificação do CID'
        verbose_name_plural = 'Classificações dos CIDs'

    def __str__(self):
        return self.descricao if self.descricao else f"Classificação #{self.cd_classificacao}"


class Cid(models.Model):
    cd_cid = models.CharField(primary_key=True, max_length=8, db_column='cd_cid')
    nm_cid = models.TextField(db_column='nm_cid')
    tp_agravo = models.SmallIntegerField(
        db_column='tp_agravo',
        db_comment='0 - Sem Agravo\n1 - Agravo de notificação\n2 - Agravo de bloqueio'
    )
    tp_sexo = models.CharField(max_length=1, db_column='tp_sexo', db_comment='M - Masculino\nF - Feminino\nI - Indiferente/Ambos')
    version = models.BigIntegerField(db_column='version')
    cd_classificacao = models.ForeignKey(CidClassificacao, models.DO_NOTHING, db_column='cd_classificacao', blank=True, null=True)
    flag_cid_categoria = models.CharField(max_length=1, db_column='flag_cid_categoria')
    ativo = models.SmallIntegerField(blank=True, null=True, db_column='ativo')
    flag_registro_diarreia = models.SmallIntegerField(blank=True, null=True, db_column='flag_registro_diarreia')

    class Meta:
        managed = False
        db_table = 'cid'
        verbose_name = 'CID (Doença)'
        verbose_name_plural = 'CIDs (Doenças)'
        db_table_comment = 'Cadastro internacional de doenças'

    def __str__(self):
        return f"{self.cd_cid} - {self.nm_cid[:50]}"


class Ciap(models.Model):
    cd_ciap = models.BigIntegerField(primary_key=True, db_column='cd_ciap')
    referencia = models.TextField(db_column='referencia')
    componente = models.SmallIntegerField(db_column='componente')
    capitulo = models.TextField(db_column='capitulo')
    titulo_original = models.TextField(db_column='titulo_original')
    titulo_leigo = models.TextField(db_column='titulo_leigo')
    cd_cid_mais_frequente = models.ForeignKey(Cid, models.DO_NOTHING, db_column='cd_cid_mais_frequente', blank=True, null=True)
    definicao = models.TextField(blank=True, null=True, db_column='definicao')
    criterios_inclusao = models.TextField(blank=True, null=True, db_column='criterios_inclusao')
    criterios_exclusao = models.TextField(blank=True, null=True, db_column='criterios_exclusao')
    considerar = models.TextField(blank=True, null=True, db_column='considerar')
    nota = models.TextField(blank=True, null=True, db_column='nota')
    version = models.BigIntegerField(db_column='version')
    situacao = models.SmallIntegerField(db_column='situacao')
    cd_us_esus = models.TextField(blank=True, null=True, db_column='cd_esus')

    class Meta:
        managed = False
        db_table = 'ciap'
        verbose_name = 'CIAP (Atenção Primária)'
        verbose_name_plural = 'CIAPs (Atenção Primária)'

    def __str__(self):
        return f"{self.referencia} - {self.titulo_original[:50]}"