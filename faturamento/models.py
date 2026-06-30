from django.db import models
import uuid6


class Procedimento(models.Model):
    class Meta: 
        managed = False
        db_table = 'procedimento'

    def __str__(self):
        return f"Procedimento {self.pk}"


class ProcedimentoFinanciamento(models.Model):
    class Meta: 
        managed = False
        db_table = 'procedimento_financiamento'

    def __str__(self):
        return f"Financiamento {self.pk}"


class ProcedimentoRubrica(models.Model):
    class Meta: 
        managed = False
        db_table = 'procedimento_rubrica'

    def __str__(self):
        return f"Rubrica {self.pk}"


class ProcedimentoFormaOrganizacao(models.Model):
    class Meta: 
        managed = False
        db_table = 'procedimento_forma_organizacao'

    def __str__(self):
        return f"Forma de Organização {self.pk}"


class ProcedimentoCompetencia(models.Model):
    public_id = models.UUIDField(default=uuid6.uuid7, editable=False, unique=True, db_index=True, db_column='uuid_publico')
    cd_procedimento = models.ForeignKey('Procedimento', models.DO_NOTHING, db_column='cd_procedimento', primary_key=True)
    dt_competencia = models.DateField()
    cd_financiamento = models.ForeignKey('ProcedimentoFinanciamento', models.DO_NOTHING, db_column='cd_financiamento', blank=True, null=True)
    cd_rubrica = models.ForeignKey('ProcedimentoRubrica', models.DO_NOTHING, db_column='cd_rubrica', blank=True, null=True)
    cd_grupo = models.ForeignKey('ProcedimentoFormaOrganizacao', models.DO_NOTHING, db_column='cd_grupo')
    cd_subgrupo = models.IntegerField()
    cd_forma_organizacao = models.IntegerField()
    tp_complexidade = models.SmallIntegerField(db_comment='0 - Não se aplica\n1 - Atenção Básica Complexidade\n2 - Média Complexidade\n3 - Alta Complexidade')
    tp_sexo = models.CharField(max_length=1, db_comment='M - Masculino\nF - Feminino\nI - Indiferente/Ambos\nN - Não se aplica')
    qt_maxima_execucao = models.DecimalField(max_digits=4, decimal_places=0, db_comment='Número máximo de execuções permitidas.\n9999 se não se aplica')
    qt_dias_permanencia = models.DecimalField(max_digits=4, decimal_places=0, db_comment='Número máximo de dias de internações possíveis.\n9999 se não se aplica')
    qt_pontos = models.DecimalField(max_digits=4, decimal_places=0, db_comment='Quantidade de pontos para o procedimento.\n9999 se não se aplica')
    vl_idade_minima = models.DecimalField(max_digits=4, decimal_places=0, db_comment='De 0000 a 1331 meses. 9999 se não se aplica.')
    vl_idade_maxima = models.DecimalField(max_digits=4, decimal_places=0, db_comment='De 0000 a 1331 meses. 9999 se não se aplica.')
    vl_sh = models.DecimalField(max_digits=12, decimal_places=2, db_comment='Valor pago para o serviço hospitalar deste procedimento.')
    vl_sa = models.DecimalField(max_digits=12, decimal_places=2, db_comment='Valor pago para o serviço ambulatorial deste procedimento.')
    vl_sp = models.DecimalField(max_digits=12, decimal_places=2, db_comment='Valor pago para o serviço profissional deste procedimento.')
    utilizado = models.CharField(max_length=1, blank=True, null=True)
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'procedimento_competencia'
        db_table_comment = 'Procedimento realizados para faturamento'
        unique_together = (('cd_procedimento', 'dt_competencia'),)

    def __str__(self):
        return f"Proc: {self.cd_procedimento} - Comp: {self.dt_competencia}"


class Convenio(models.Model):
    cd_convenio = models.BigIntegerField(primary_key=True)
    public_id = models.UUIDField(default=uuid6.uuid7, editable=False, unique=True, db_index=True, db_column='uuid_publico')
    ds_convenio = models.CharField(max_length=50)
    version = models.BigIntegerField()
    cd_convenio_pai = models.ForeignKey('self', models.DO_NOTHING, db_column='cd_convenio_pai', blank=True, null=True)
    razao_social = models.CharField(max_length=100, blank=True, null=True)
    nome_fantasia = models.CharField(max_length=100, blank=True, null=True)
    cnpj = models.CharField(max_length=14, blank=True, null=True)
    inscricao_estadual = models.CharField(max_length=9, blank=True, null=True)
    endereco = models.CharField(max_length=200, blank=True, null=True)
    telefone = models.CharField(max_length=11, blank=True, null=True)
    telefone2 = models.CharField(max_length=11, blank=True, null=True)
    cidade = models.ForeignKey('Cidade', models.DO_NOTHING, db_column='cidade', blank=True, null=True)
    subconvenio = models.SmallIntegerField()
    validacao_nr_convenio = models.SmallIntegerField(blank=True, null=True)
    flag_nr_convenio_obrigatorio = models.SmallIntegerField(blank=True, null=True)
    cd_tp_tabela = models.ForeignKey('TipoTabelaProcedimento', models.DO_NOTHING, db_column='cd_tp_tabela')
    registro_ans_orig = models.CharField(max_length=6, blank=True, null=True)
    registro_ans_dest = models.CharField(max_length=6, blank=True, null=True)
    cd_gerenciador_arquivo = models.ForeignKey('GerenciadorArquivo', models.DO_NOTHING, db_column='cd_gerenciador_arquivo', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'convenio'
        unique_together = (('ds_convenio', 'subconvenio'),)

    def __str__(self):
        return f"{self.cd_convenio} - {self.nome_fantasia or self.ds_convenio}"


class TipoProcedimentoAtendimento(models.Model):
    cd_procedimento_atendimento = models.BigIntegerField(primary_key=True)
    public_id = models.UUIDField(default=uuid6.uuid7, editable=False, unique=True, db_index=True, db_column='uuid_publico')
    ds_procedimento_atendimento = models.CharField(max_length=50)
    version = models.BigIntegerField()
    flag_reserva = models.SmallIntegerField()
    flag_exibir_pagina = models.SmallIntegerField()
    cd_nat_proc_tp_atendimento_ag = models.ForeignKey('NaturezaProcuraTpAtendimento', models.DO_NOTHING, db_column='cd_nat_proc_tp_atendimento_ag', blank=True, null=True)
    cd_nat_proc_tp_atendimento_at = models.ForeignKey('NaturezaProcuraTpAtendimento', models.DO_NOTHING, db_column='cd_nat_proc_tp_atendimento_at', related_name='tipoprocedimentoatendimento_cd_nat_proc_tp_atendimento_at_set', blank=True, null=True)
    flag_fila_procedimentos = models.SmallIntegerField(blank=True, null=True)
    flag_dis_confirmacao_presenca = models.SmallIntegerField(blank=True, null=True)
    flag_marcacao_consulta = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_procedimento_atendimento'

    def __str__(self):
        return self.ds_procedimento_atendimento


# =====================================================================
# STUBS TEMPORÁRIOS PARA ESTE APP
# =====================================================================
class Cidade(models.Model):
    class Meta: 
        managed = False
        db_table = 'cidade'

class TipoTabelaProcedimento(models.Model):
    class Meta: 
        managed = False
        db_table = 'tipo_tabela_procedimento'

class GerenciadorArquivo(models.Model):
    class Meta: 
        managed = False
        db_table = 'gerenciador_arquivo'

class NaturezaProcuraTpAtendimento(models.Model):
    class Meta: 
        managed = False
        db_table = 'natureza_procura_tp_atendimento'