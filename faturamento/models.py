from django.db import models

class Procedimento(models.Model):
    cd_procedimento = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0, db_column='cd_procedimento')
    ds_procedimento = models.CharField(max_length=512, db_column='ds_procedimento')
    situacao = models.CharField(max_length=1, blank=True, null=True, db_column='situacao')
    faturavel = models.CharField(max_length=1, blank=True, null=True, db_column='faturavel')
    version = models.BigIntegerField(db_column='version')
    
    # BLINDAGEM: Isolados como IntegerField para não colidir com a chave composta de ProcedimentoFormaOrganizacao
    cd_grupo = models.IntegerField(blank=True, null=True, db_column='cd_grupo')
    cd_subgrupo = models.IntegerField(blank=True, null=True, db_column='cd_subgrupo')
    cd_forma_organizacao = models.IntegerField(blank=True, null=True, db_column='cd_forma_organizacao')
    
    # Desacoplamento de string limpa para o catálogo do CBO
    cd_cbo_bpa = models.CharField(max_length=10, blank=True, null=True, db_column='cd_cbo_bpa')
    referencia = models.CharField(max_length=20, blank=True, null=True, db_column='referencia')
    
    # Relacionamentos Cross-App amarrados com segurança por string
    empresa_bpa = models.ForeignKey('institucional.Empresa', models.DO_NOTHING, db_column='empresa_bpa', blank=True, null=True)
    cd_profissional_bpa = models.ForeignKey('profissionais.Profissional', models.DO_NOTHING, db_column='cd_profissional_bpa', blank=True, null=True)
    cd_tp_tabela = models.ForeignKey('TipoTabelaProcedimento', models.DO_NOTHING, db_column='cd_tp_tabela')
    
    flag_val_cns = models.SmallIntegerField(blank=True, null=True, db_column='flag_val_cns')
    
    # Isolamento de campo financeiro não mapeado
    cd_tp_mov_cta_financeira = models.BigIntegerField(blank=True, null=True, db_column='cd_tp_mov_cta_financeira')
    flag_consulta_esus = models.SmallIntegerField(db_column='flag_consulta_esus')

    class Meta:
        managed = False
        db_table = 'procedimento'
        verbose_name = 'Procedimento (SIGTAP)'
        verbose_name_plural = 'Procedimentos (SIGTAP)'
        db_table_comment = 'Procedimento realizados para faturamento'

    def __str__(self):
        # Transforma o Decimal em int para remover o '.0' da exibição do código SUS
        return f"{int(self.cd_procedimento)} - {self.ds_procedimento[:50]}"
    

class ProcedimentoFinanciamento(models.Model):
    cd_financiamento = models.IntegerField(primary_key=True, db_column='cd_financiamento')
    ds_financiamento = models.CharField(max_length=100, db_column='ds_financiamento')
    dt_competencia = models.DateField(db_column='dt_competencia')
    version = models.BigIntegerField(db_column='version')

    class Meta:
        managed = False
        db_table = 'procedimento_financiamento'
        verbose_name = 'Financiamento do Procedimento'
        verbose_name_plural = 'Financiamentos dos Procedimentos'

    def __str__(self):
        return self.ds_financiamento