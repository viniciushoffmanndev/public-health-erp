# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from pacientes.models import UsuarioCadsus
import uuid6


class AcaoProgramaticaGrupo(models.Model): # Tabela não foi inspecionada 
    class Meta: 
        managed = False
        db_table = 'acao_programatica_grupo'
    
    def __str__(self):
        return f"Grupo Programático {self.pk}"


class ClassificacaoAtendimento(models.Model):
    class Meta: 
        managed = False
        db_table = 'classificacao_atendimento'
    
    def __str__(self):
        return f"Classificação {self.pk}"


class Conduta(models.Model):
    class Meta: 
        managed = False
        db_table = 'conduta'
    
    def __str__(self):
        return f"Conduta {self.pk}"


class Atendimento(models.Model):
    nr_atendimento = models.BigIntegerField(primary_key=True)
    #public_id = models.UUIDField(default=uuid6.uuid7, editable=False, unique=True, db_index=True,db_column='uuid_publico')
    empresa = models.ForeignKey('institucional.Empresa', models.DO_NOTHING, db_column='empresa')
    cd_usu_cadsus = models.ForeignKey(UsuarioCadsus, models.DO_NOTHING, db_column='cd_usu_cadsus', blank=True, null=True)
    dt_chegada = models.DateTimeField(blank=True, null=True, db_comment='data do registro do paciente na unidade.')
    dt_atendimento = models.DateTimeField(blank=True, null=True)
    dt_fechamento = models.DateTimeField(blank=True, null=True, db_comment='Data da solucao do prontuario.')
    status = models.IntegerField()
    dt_cancelamento = models.DateTimeField(blank=True, null=True)
    ds_obs_cancelamento = models.CharField(max_length=300, blank=True, null=True)
    cod_motivo = models.ForeignKey('triagem.MotivosCancelamento', models.DO_NOTHING, db_column='cod_motivo', blank=True, null=True)
    cd_usuario_can = models.ForeignKey('profissionais.Usuarios', models.DO_NOTHING, db_column='cd_usuario_can', blank=True, null=True)
    nr_prox_atendimento = models.ForeignKey('self', models.DO_NOTHING, db_column='nr_prox_atendimento', blank=True, null=True)
    cd_procedimento = models.ForeignKey('faturamento.ProcedimentoCompetencia', models.DO_NOTHING, db_column='cd_procedimento')
    dt_competencia = models.DateField()
    cd_acao_programatica = models.ForeignKey('AcaoProgramaticaGrupo', models.DO_NOTHING, db_column='cd_acao_programatica', blank=True, null=True)
    cd_grupo_atendimento = models.BigIntegerField(blank=True, null=True)
    cd_profissional = models.ForeignKey('profissionais.Profissional', models.DO_NOTHING, db_column='cd_profissional', blank=True, null=True)
    cd_usuario = models.ForeignKey('profissionais.Usuarios', models.DO_NOTHING, db_column='cd_usuario', related_name='atendimento_cd_usuario_set')
    nr_atendimento_origem = models.ForeignKey('self', models.DO_NOTHING, db_column='nr_atendimento_origem', related_name='atendimento_nr_atendimento_origem_set', blank=True, null=True)
    cd_cbo = models.ForeignKey('profissionais.TabelaCbo', models.DO_NOTHING, db_column='cd_cbo', blank=True, null=True)
    cd_profissional_responsavel = models.ForeignKey('profissionais.Profissional', models.DO_NOTHING, db_column='cd_profissional_responsavel', related_name='atendimento_cd_profissional_responsavel_set', blank=True, null=True)
    cd_cid_principal = models.ForeignKey('diagnosticos.Cid', models.DO_NOTHING, db_column='cd_cid_principal', blank=True, null=True)
    cd_cid_secundario = models.ForeignKey('diagnosticos.Cid', models.DO_NOTHING, db_column='cd_cid_secundario', related_name='atendimento_cd_cid_secundario_set', blank=True, null=True)
    cd_cla_atendimento = models.ForeignKey('ClassificacaoAtendimento', models.DO_NOTHING, db_column='cd_cla_atendimento', blank=True, null=True)
    cd_conduta = models.ForeignKey('Conduta', models.DO_NOTHING, db_column='cd_conduta', blank=True, null=True)
    dt_imp_prontuario = models.DateTimeField(blank=True, null=True)
    dt_observacao = models.DateTimeField(blank=True, null=True)
    cd_domicilio = models.ForeignKey('geografia.EnderecoDomicilio', models.DO_NOTHING, db_column='cd_domicilio', blank=True, null=True)
    cd_endereco = models.ForeignKey('EnderecoUsuarioCadsus', models.DO_NOTHING, db_column='cd_endereco', blank=True, null=True)
    nr_atendimento_principal = models.ForeignKey('self', models.DO_NOTHING, db_column='nr_atendimento_principal', related_name='atendimento_nr_atendimento_principal_set')
    dt_alta = models.DateTimeField(blank=True, null=True)
    seq_ciclo = models.IntegerField(blank=True, null=True)
    competencia_atendimento = models.DateField(blank=True, null=True)
    dia_retorno = models.SmallIntegerField(blank=True, null=True)
    ds_obs_retorno = models.CharField(blank=True, null=True)
    nm_paciente = models.CharField(max_length=140, blank=True, null=True)
    version = models.BigIntegerField()
    cd_nat_proc_tp_atendimento = models.ForeignKey('NaturezaProcuraTpAtendimento', models.DO_NOTHING, db_column='cd_nat_proc_tp_atendimento')
    tp_demanda = models.SmallIntegerField()
    prioridade = models.SmallIntegerField()
    cd_leito = models.ForeignKey('LeitoQuarto', models.DO_NOTHING, db_column='cd_leito', blank=True, null=True)
    cd_convenio = models.ForeignKey('Convenio', models.DO_NOTHING, db_column='cd_convenio', blank=True, null=True)
    enc_alta = models.BigIntegerField(blank=True, null=True)
    cd_usu_cadsus_responsavel = models.ForeignKey(UsuarioCadsus, models.DO_NOTHING, db_column='cd_usu_cadsus_responsavel', related_name='atendimento_cd_usu_cadsus_responsavel_set', blank=True, null=True)
    numero_registro_convenio = models.CharField(max_length=50, blank=True, null=True)
    classificacao_risco = models.ForeignKey('ClassificacaoRisco', models.DO_NOTHING, db_column='classificacao_risco', blank=True, null=True)
    dt_cadastro = models.DateTimeField(blank=True, null=True)
    cd_procedimento_atendimento = models.ForeignKey('TipoProcedimentoAtendimento', models.DO_NOTHING, db_column='cd_procedimento_atendimento', blank=True, null=True)
    empresa_bpa = models.ForeignKey('institucional.Empresa', models.DO_NOTHING, db_column='empresa_bpa', related_name='atendimento_empresa_bpa_set')
    vacina_em_dia = models.SmallIntegerField(blank=True, null=True)
    observacao_marcacao = models.CharField(max_length=500, blank=True, null=True)
    correcao = models.SmallIntegerField(blank=True, null=True)
    paralelo = models.SmallIntegerField(blank=True, null=True)
    dt_validade_convenio = models.DateField(blank=True, null=True)
    empresa_solicitante = models.ForeignKey('institucional.Empresa', models.DO_NOTHING, db_column='empresa_solicitante', related_name='atendimento_empresa_solicitante_set', blank=True, null=True)
    cd_usuario_atendendo = models.ForeignKey('profissionais.Usuarios', models.DO_NOTHING, db_column='cd_usuario_atendendo', related_name='atendimento_cd_usuario_atendendo_set', blank=True, null=True)
    dt_integracao_inovamfri = models.DateTimeField(blank=True, null=True)
    cd_ciap = models.ForeignKey('Ciap', models.DO_NOTHING, db_column='cd_ciap', blank=True, null=True)
    flag_gestante = models.SmallIntegerField(blank=True, null=True)
    cd_atv_grupo = models.ForeignKey('AtividadeGrupo', models.DO_NOTHING, db_column='cd_atv_grupo', blank=True, null=True)
    pic = models.IntegerField(blank=True, null=True)
    nasfs = models.IntegerField(blank=True, null=True)
    local_atendimento = models.SmallIntegerField(blank=True, null=True)
    racionalidade_saude = models.SmallIntegerField(blank=True, null=True)
    cd_profissional_auxiliar = models.ForeignKey('profissionais.Profissional', models.DO_NOTHING, db_column='cd_profissional_auxiliar', related_name='atendimento_cd_profissional_auxiliar_set', blank=True, null=True)
    tp_atendimento_odonto = models.SmallIntegerField(blank=True, null=True)
    tp_consulta_odonto = models.SmallIntegerField(blank=True, null=True)
    tp_fornecimento_odonto = models.SmallIntegerField(blank=True, null=True)
    cod_tp_consulta = models.SmallIntegerField(blank=True, null=True)
    tp_atencao_domiciliar = models.SmallIntegerField(blank=True, null=True)
    tp_atendimento_esus = models.SmallIntegerField(blank=True, null=True)
    dum_gestante = models.DateField(blank=True, null=True)
    gravidez_planejada = models.SmallIntegerField(blank=True, null=True)
    idade_gestacional = models.SmallIntegerField(blank=True, null=True)
    nr_gestas_previas = models.SmallIntegerField(blank=True, null=True)
    nr_partos = models.SmallIntegerField(blank=True, null=True)
    cd_cbo_auxiliar = models.ForeignKey('profissionais.TabelaCbo', models.DO_NOTHING, db_column='cd_cbo_auxiliar', related_name='atendimento_cd_cbo_auxiliar_set', blank=True, null=True)
    valor_subclassificacao_risco = models.SmallIntegerField(blank=True, null=True)
    ds_subclassificacao_risco = models.CharField(max_length=20, blank=True, null=True)
    dt_chamada = models.DateTimeField(blank=True, null=True)
    cd_profissional_chamada = models.ForeignKey('profissionais.Profissional', models.DO_NOTHING, db_column='cd_profissional_chamada', related_name='atendimento_cd_profissional_chamada_set', blank=True, null=True)
    cd_estabelecimento_cerest = models.ForeignKey('EstabelecimentoCerest', models.DO_NOTHING, db_column='cd_estabelecimento_cerest', blank=True, null=True)
    flag_permite_reclassificacao = models.SmallIntegerField(blank=True, null=True)
    dt_reclassificacao = models.DateTimeField(blank=True, null=True)
    dt_canc_lote = models.DateTimeField(blank=True, null=True)
    flag_consulta = models.SmallIntegerField(blank=True, null=True)
    cd_equipe = models.ForeignKey('Equipe', models.DO_NOTHING, db_column='cd_equipe', blank=True, null=True)
    dt_inicio_agendamento = models.DateTimeField(blank=True, null=True)
    dt_fim_agendamento = models.DateTimeField(blank=True, null=True)
    flag_preencheu_notificacao = models.SmallIntegerField(blank=True, null=True)
    nr_gestas_vaginal = models.SmallIntegerField(blank=True, null=True)
    nr_gestas_cesariana = models.SmallIntegerField(blank=True, null=True)
    nr_gestas_aborto = models.SmallIntegerField(blank=True, null=True)
    dt_primeira_usg = models.DateField(blank=True, null=True)
    idade_gestacional_usg = models.SmallIntegerField(blank=True, null=True)
    dpp_dum = models.DateField(blank=True, null=True)
    dpp_usg = models.DateField(blank=True, null=True)
    conduta_covid = models.SmallIntegerField(blank=True, null=True)
    cns = models.BigIntegerField(blank=True, null=True)
    cpf = models.CharField(max_length=11, blank=True, null=True)
    motivo_consulta = models.CharField(max_length=50, blank=True, null=True)
    nr_senha = models.IntegerField(blank=True, null=True)
    tp_senha = models.SmallIntegerField(blank=True, null=True)
    tipo_participacao_cidadao = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'atendimento'

    def __str__(self):
        return f"Atendimento {self.nr_atendimento} - {self.nm_paciente or 'Sem Nome'}"


# =====================================================================
# STUBS TEMPORÁRIOS PARA ESTE APP (Até fazermos o inspectdb delas)
# =====================================================================
class EnderecoUsuarioCadsus(models.Model):
    class Meta: 
        managed = False
        db_table = 'endereco_usuario_cadsus'

class NaturezaProcuraTpAtendimento(models.Model):
    class Meta: 
        managed = False
        db_table = 'natureza_procura_tp_atendimento'

class LeitoQuarto(models.Model):
    class Meta: 
        managed = False
        db_table = 'leito_quarto'

class Convenio(models.Model):
    class Meta: 
        managed = False
        db_table = 'convenio'

class ClassificacaoRisco(models.Model):
    class Meta: 
        managed = False
        db_table = 'classificacao_risco'

class TipoProcedimentoAtendimento(models.Model):
    class Meta: 
        managed = False
        db_table = 'tipo_procedimento_atendimento'

class Ciap(models.Model):
    class Meta: 
        managed = False
        db_table = 'ciap'

class AtividadeGrupo(models.Model):
    class Meta: 
        managed = False
        db_table = 'atividade_grupo'

class EstabelecimentoCerest(models.Model):
    class Meta: 
        managed = False
        db_table = 'estabelecimento_cerest'

class Equipe(models.Model):
    class Meta: 
        managed = False
        db_table = 'equipe'
