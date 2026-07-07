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


class AcaoProgramaticaGrupo(models.Model):
    cd_acao_programatica = models.BigIntegerField(primary_key=True, db_column='cd_acao_programatica')
    cd_grupo_atendimento = models.BigIntegerField(db_column='cd_grupo_atendimento')
    version = models.BigIntegerField(db_column='version')

    class Meta:
        managed = False
        db_table = 'acao_programatica_grupo'
        verbose_name = 'Grupo de Ação Programática'
        verbose_name_plural = 'Grupos de Ações Programáticas'

    def __str__(self):
        return f"Ação {self.cd_acao_programatica} - Grupo {self.cd_grupo_atendimento}"


class ClassificacaoAtendimento(models.Model):
    cd_cla_atendimento = models.IntegerField(primary_key=True, db_column='cd_cla_atendimento')
    ds_cla_atendimento = models.CharField(max_length=50, db_column='ds_cla_atendimento')
    cd_procedimento = models.BigIntegerField(blank=True, null=True, db_column='cd_procedimento')
    cd_siab = models.BigIntegerField(blank=True, null=True, db_column='cd_siab')
    version = models.BigIntegerField(db_column='version')
    ordem = models.SmallIntegerField(db_column='ordem')
    cd_esus = models.CharField(max_length=20, blank=True, null=True, db_column='cd_esus')
    classificacao_esus = models.SmallIntegerField(blank=True, null=True, db_column='classificacao_esus')
    situacao = models.SmallIntegerField(db_column='situacao')
    flag_exibe_encaminhamento_alta = models.SmallIntegerField(db_column='flag_exibe_encaminhamento_alta')

    class Meta:
        managed = False
        db_table = 'classificacao_atendimento'
        verbose_name = 'Classificação de Atendimento'
        verbose_name_plural = 'Classificações de Atendimentos'

    def __str__(self):
        return self.ds_cla_atendimento


class Conduta(models.Model):
    cd_conduta = models.IntegerField(primary_key=True, db_column='cd_conduta')
    ds_conduta = models.CharField(max_length=50, db_column='ds_conduta')
    gera_encaminhamento = models.CharField(max_length=1, blank=True, null=True, db_column='gera_encaminhamento')
    version = models.BigIntegerField(db_column='version')
    cd_esus = models.SmallIntegerField(blank=True, null=True, db_column='cd_esus')
    classificacao_esus = models.SmallIntegerField(blank=True, null=True, db_column='classificacao_esus')
    tp_conduta = models.SmallIntegerField(blank=True, null=True, db_column='tp_conduta')
    flag_retorno = models.SmallIntegerField(db_column='flag_retorno')

    class Meta:
        managed = False
        db_table = 'conduta'
        verbose_name = 'Conduta de Atendimento'
        verbose_name_plural = 'Condutas de Atendimento'

    def __str__(self):
        return self.ds_conduta


class NaturezaProcuraTpAtendimento(models.Model):
    cd_nat_proc_tp_atendimento = models.BigIntegerField(primary_key=True, db_column='cd_nat_proc_tp_atendimento')
    cd_nat_procura = models.BigIntegerField(db_column='cd_nat_procura')
    cd_tp_atendimento = models.BigIntegerField(db_column='cd_tp_atendimento')
    cd_tp_procedimento = models.BigIntegerField(blank=True, null=True, db_column='cd_tp_procedimento')
    version = models.BigIntegerField(db_column='version')
    visivel = models.CharField(max_length=1, blank=True, null=True, db_column='visivel')
    imprime_termo_autorizacao = models.SmallIntegerField(blank=True, null=True, db_column='imprime_termo_autorizacao')
    imprime_ficha_paciente = models.SmallIntegerField(db_column='imprime_ficha_paciente')
    cd_tp_exame = models.IntegerField(blank=True, null=True, db_column='cd_tp_exame')

    class Meta:
        managed = False
        db_table = 'natureza_procura_tp_atendimento'
        verbose_name = 'Natureza de Procura por Tipo de Atendimento'
        verbose_name_plural = 'Naturezas de Procura por Tipo de Atendimento'

    def __str__(self):
        return f"Configuração de Recepção #{self.cd_nat_proc_tp_atendimento}"


class LeitoQuarto(models.Model):
    cd_leito = models.BigIntegerField(primary_key=True, db_column='cd_leito')
    cd_quarto_internacao = models.BigIntegerField(db_column='cd_quarto_internacao')
    ds_leito = models.CharField(max_length=50, db_column='ds_leito')
    situacao = models.SmallIntegerField(db_column='situacao')
    version = models.BigIntegerField(db_column='version')
    nr_atendimento = models.ForeignKey('Atendimento', models.DO_NOTHING, db_column='nr_atendimento', blank=True, null=True)
    dt_cadastro = models.DateTimeField(db_column='dt_cadastro')
    dt_exclusao = models.DateTimeField(blank=True, null=True, db_column='dt_exclusao')
    cd_usuario_cad = models.ForeignKey('profissionais.Usuarios', models.DO_NOTHING, db_column='cd_usuario_cad')
    cd_usuario_exc = models.ForeignKey('profissionais.Usuarios', models.DO_NOTHING, db_column='cd_usuario_exc', related_name='leitoquarto_cd_usuario_exc_set', blank=True, null=True)
    numero_leito_aih = models.CharField(max_length=4, blank=True, null=True, db_column='numero_leito_aih')
    cd_especialidade = models.IntegerField(blank=True, null=True, db_column='cd_especialidade')
    dt_desativacao = models.DateField(blank=True, null=True, db_column='dt_desativacao')
    motivo = models.TextField(blank=True, null=True, db_column='motivo')
    cd_usu_cadsus = models.ForeignKey('pacientes.UsuarioCadsus', models.DO_NOTHING, db_column='cd_usu_cadsus', blank=True, null=True)
    cd_aut_intern_hosp = models.BigIntegerField(blank=True, null=True, db_column='cd_aut_intern_hosp')
    sexo = models.BigIntegerField(blank=True, null=True, db_column='sexo')
    tipo_leito = models.BigIntegerField(blank=True, null=True, db_column='tipo_leito')
    cd_aut_intern_hosp_secundaria = models.BigIntegerField(blank=True, null=True, db_column='cd_aut_intern_hosp_secundaria')

    class Meta:
        managed = False
        db_table = 'leito_quarto'
        verbose_name = 'Leito / Quarto'
        verbose_name_plural = 'Leitos / Quartos'

    def __str__(self):
        return self.ds_leito


class AtividadeGrupo(models.Model):
    cd_atv_grupo = models.BigIntegerField(primary_key=True, db_column='cd_atv_grupo')
    empresa = models.ForeignKey('institucional.Empresa', models.DO_NOTHING, db_column='empresa')
    cd_tp_atv_grupo = models.BigIntegerField(db_column='cd_tp_atv_grupo')
    data_hora_inicio = models.DateTimeField(db_column='data_hora_inicio')
    data_hora_fim = models.DateTimeField(blank=True, null=True, db_column='data_hora_fim')
    assunto = models.CharField(max_length=1000, blank=True, null=True, db_column='assunto')
    dt_cadastro = models.DateTimeField(db_column='dt_cadastro')
    situacao = models.SmallIntegerField(db_column='situacao')
    cd_local_acao = models.BigIntegerField(blank=True, null=True, db_column='cd_local_acao')
    dt_baixa = models.DateTimeField(blank=True, null=True, db_column='dt_baixa')
    cd_usu_baixa = models.ForeignKey('profissionais.Usuarios', models.DO_NOTHING, db_column='cd_usu_baixa', blank=True, null=True)
    motivo = models.CharField(max_length=200, blank=True, null=True, db_column='motivo')
    dt_cancelamento = models.DateTimeField(blank=True, null=True, db_column='dt_cancelamento')
    observacao_fechamento = models.CharField(blank=True, null=True, db_column='observacao_fechamento')
    version = models.BigIntegerField(db_column='version')
    qtd_participantes = models.IntegerField(blank=True, null=True, db_column='qtd_participantes')
    nr_inep = models.BigIntegerField(blank=True, null=True, db_column='nr_inep')
    flag_origem = models.SmallIntegerField(db_column='flag_origem')
    cd_empresa_bpa = models.ForeignKey('institucional.Empresa', models.DO_NOTHING, db_column='cd_empresa_bpa', related_name='atividadegrupo_cd_empresa_bpa_set')
    turno = models.SmallIntegerField(blank=True, null=True, db_column='turno')
    cd_outro_procedimento_esus = models.BigIntegerField(blank=True, null=True, db_column='cd_outro_procedimento_esus')
    cd_outro_proc_coletivo = models.BigIntegerField(blank=True, null=True, db_column='cd_outro_proc_coletivo')
    ds_ata = models.CharField(blank=True, null=True, db_column='ds_ata')
    pse_educacao = models.SmallIntegerField(blank=True, null=True, db_column='pse_educacao')
    pse_saude = models.SmallIntegerField(blank=True, null=True, db_column='pse_saude')
    uuid_tablet = models.CharField(blank=True, null=True, db_column='uuid_tablet')

    class Meta:
        managed = False
        db_table = 'atividade_grupo'
        verbose_name = 'Atividade em Grupo'
        verbose_name_plural = 'Atividades em Grupo'

    def __str__(self):
        return self.assunto if self.assunto else f"Atividade Coletiva #{self.cd_atv_grupo}"


class Atendimento(models.Model):
    nr_atendimento = models.BigIntegerField(primary_key=True, db_column='nr_atendimento')
    empresa = models.ForeignKey('institucional.Empresa', models.DO_NOTHING, db_column='empresa')
    cd_usu_cadsus = models.ForeignKey(UsuarioCadsus, models.DO_NOTHING, db_column='cd_usu_cadsus', blank=True, null=True)
    dt_chegada = models.DateTimeField(blank=True, null=True, db_column='dt_chegada')
    dt_atendimento = models.DateTimeField(blank=True, null=True, db_column='dt_atendimento')
    dt_fechamento = models.DateTimeField(blank=True, null=True, db_column='dt_fechamento')
    status = models.IntegerField(db_column='status')
    dt_cancelamento = models.DateTimeField(blank=True, null=True, db_column='dt_cancelamento')
    ds_obs_cancelamento = models.CharField(max_length=300, blank=True, null=True, db_column='ds_obs_cancelamento')
    cod_motivo = models.ForeignKey('triagem.MotivosCancelamento', models.DO_NOTHING, db_column='cod_motivo', blank=True, null=True)
    cd_usuario_can = models.ForeignKey('profissionais.Usuarios', models.DO_NOTHING, db_column='cd_usuario_can', blank=True, null=True)
    nr_prox_atendimento = models.ForeignKey('self', models.DO_NOTHING, db_column='nr_prox_atendimento', blank=True, null=True)
    cd_procedimento = models.ForeignKey('faturamento.ProcedimentoCompetencia', models.DO_NOTHING, db_column='cd_procedimento')
    dt_competencia = models.DateField(db_column='dt_competencia')
    cd_acao_programatica = models.ForeignKey('AcaoProgramaticaGrupo', models.DO_NOTHING, db_column='cd_acao_programatica', blank=True, null=True)
    cd_grupo_atendimento = models.BigIntegerField(blank=True, null=True, db_column='cd_grupo_atendimento')
    cd_profissional = models.ForeignKey('profissionais.Profissional', models.DO_NOTHING, db_column='cd_profissional', blank=True, null=True)
    cd_usuario = models.ForeignKey('profissionais.Usuarios', models.DO_NOTHING, db_column='cd_usuario', related_name='atendimento_cd_usuario_set')
    nr_atendimento_origem = models.ForeignKey('self', models.DO_NOTHING, db_column='nr_atendimento_origem', related_name='atendimento_nr_atendimento_origem_set', blank=True, null=True)
    cd_cbo = models.ForeignKey('profissionais.TabelaCbo', models.DO_NOTHING, db_column='cd_cbo', blank=True, null=True)
    cd_profissional_responsavel = models.ForeignKey('profissionais.Profissional', models.DO_NOTHING, db_column='cd_profissional_responsavel', related_name='atendimento_cd_profissional_responsavel_set', blank=True, null=True)
    cd_cid_principal = models.ForeignKey('diagnosticos.Cid', models.DO_NOTHING, db_column='cd_cid_principal', blank=True, null=True)
    cd_cid_secundario = models.ForeignKey('diagnosticos.Cid', models.DO_NOTHING, db_column='cd_cid_secundario', related_name='atendimento_cd_cid_secundario_set', blank=True, null=True)
    cd_cla_atendimento = models.ForeignKey('ClassificacaoAtendimento', models.DO_NOTHING, db_column='cd_cla_atendimento', blank=True, null=True)
    cd_conduta = models.ForeignKey('Conduta', models.DO_NOTHING, db_column='cd_conduta', blank=True, null=True)
    dt_imp_prontuario = models.DateTimeField(blank=True, null=True, db_column='dt_imp_prontuario')
    dt_observacao = models.DateTimeField(blank=True, null=True, db_column='dt_observacao')
    cd_domicilio = models.ForeignKey('geografia.EnderecoDomicilio', models.DO_NOTHING, db_column='cd_domicilio', blank=True, null=True)
    cd_endereco = models.ForeignKey('geografia.EnderecoUsuarioCadsus', models.DO_NOTHING, db_column='cd_endereco', blank=True, null=True)
    nr_atendimento_principal = models.ForeignKey('self', models.DO_NOTHING, db_column='nr_atendimento_principal', related_name='atendimento_nr_atendimento_principal_set')
    dt_alta = models.DateTimeField(blank=True, null=True, db_column='dt_alta')
    seq_ciclo = models.IntegerField(blank=True, null=True, db_column='seq_ciclo')
    competencia_atendimento = models.DateField(blank=True, null=True, db_column='competencia_atendimento')
    dia_retorno = models.SmallIntegerField(blank=True, null=True, db_column='dia_retorno')
    ds_obs_retorno = models.TextField(blank=True, null=True, db_column='ds_obs_retorno')
    nm_paciente = models.CharField(max_length=140, blank=True, null=True, db_column='nm_paciente')
    version = models.BigIntegerField(db_column='version')
    cd_nat_proc_tp_atendimento = models.ForeignKey('NaturezaProcuraTpAtendimento', models.DO_NOTHING, db_column='cd_nat_proc_tp_atendimento')
    tp_demanda = models.SmallIntegerField(db_column='tp_demanda')
    prioridade = models.SmallIntegerField(db_column='prioridade')
    cd_leito = models.ForeignKey('LeitoQuarto', models.DO_NOTHING, db_column='cd_leito', blank=True, null=True)
    cd_convenio = models.ForeignKey('faturamento.Convenio', models.DO_NOTHING, db_column='cd_convenio', blank=True, null=True)
    enc_alta = models.BigIntegerField(blank=True, null=True, db_column='enc_alta')
    cd_usu_cadsus_responsavel = models.ForeignKey(UsuarioCadsus, models.DO_NOTHING, db_column='cd_usu_cadsus_responsavel', related_name='atendimento_cd_usu_cadsus_responsavel_set', blank=True, null=True)
    numero_registro_convenio = models.CharField(max_length=50, blank=True, null=True, db_column='numero_registro_convenio')
    classificacao_risco = models.ForeignKey('triagem.ClassificacaoRisco', models.DO_NOTHING, db_column='classificacao_risco', blank=True, null=True)
    dt_cadastro = models.DateTimeField(blank=True, null=True, db_column='dt_cadastro')
    cd_procedimento_atendimento = models.ForeignKey('faturamento.TipoProcedimentoAtendimento', models.DO_NOTHING, db_column='cd_procedimento_atendimento', blank=True, null=True)
    empresa_bpa = models.ForeignKey('institucional.Empresa', models.DO_NOTHING, db_column='empresa_bpa', related_name='atendimento_empresa_bpa_set')
    vacina_em_dia = models.SmallIntegerField(blank=True, null=True, db_column='vacina_em_dia')
    observacao_marcacao = models.CharField(max_length=500, blank=True, null=True, db_column='observacao_marcacao')
    correcao = models.SmallIntegerField(blank=True, null=True, db_column='correcao')
    paralelo = models.SmallIntegerField(blank=True, null=True, db_column='paralelo')
    dt_validade_convenio = models.DateField(blank=True, null=True, db_column='dt_validade_convenio')
    empresa_solicitante = models.ForeignKey('institucional.Empresa', models.DO_NOTHING, db_column='empresa_solicitante', related_name='atendimento_empresa_solicitante_set', blank=True, null=True)
    cd_usuario_atendendo = models.ForeignKey('profissionais.Usuarios', models.DO_NOTHING, db_column='cd_usuario_atendendo', related_name='atendimento_cd_usuario_atendendo_set', blank=True, null=True)
    dt_integracao_inovamfri = models.DateTimeField(blank=True, null=True, db_column='dt_integracao_inovamfri')
    cd_ciap = models.ForeignKey('diagnosticos.Ciap', models.DO_NOTHING, db_column='cd_ciap', blank=True, null=True)
    flag_gestante = models.SmallIntegerField(blank=True, null=True, db_column='flag_gestante')
    cd_atv_grupo = models.ForeignKey('AtividadeGrupo', models.DO_NOTHING, db_column='cd_atv_grupo', blank=True, null=True)
    pic = models.IntegerField(blank=True, null=True, db_column='pic')
    nasfs = models.IntegerField(blank=True, null=True, db_column='nasfs')
    local_atendimento = models.SmallIntegerField(blank=True, null=True, db_column='local_atendimento')
    racionalidade_saude = models.SmallIntegerField(blank=True, null=True, db_column='racionalidade_saude')
    cd_profissional_auxiliar = models.ForeignKey('profissionais.Profissional', models.DO_NOTHING, db_column='cd_profissional_auxiliar', related_name='atendimento_cd_profissional_auxiliar_set', blank=True, null=True)
    tp_atendimento_odonto = models.SmallIntegerField(blank=True, null=True, db_column='tp_atendimento_odonto')
    tp_consulta_odonto = models.SmallIntegerField(blank=True, null=True, db_column='tp_consulta_odonto')
    tp_fornecimento_odonto = models.SmallIntegerField(blank=True, null=True, db_column='tp_fornecimento_odonto')
    cod_tp_consulta = models.SmallIntegerField(blank=True, null=True, db_column='cod_tp_consulta')
    tp_atencao_domiciliar = models.SmallIntegerField(blank=True, null=True, db_column='tp_atencao_domiciliar')
    tp_atendimento_esus = models.SmallIntegerField(blank=True, null=True, db_column='tp_atendimento_esus')
    dum_gestante = models.DateField(blank=True, null=True, db_column='dum_gestante')
    gravidez_planejada = models.SmallIntegerField(blank=True, null=True, db_column='gravidez_planejada')
    idade_gestacional = models.SmallIntegerField(blank=True, null=True, db_column='idade_gestacional')
    nr_gestas_previas = models.SmallIntegerField(blank=True, null=True, db_column='nr_gestas_previas')
    nr_partos = models.SmallIntegerField(blank=True, null=True, db_column='nr_partos')
    cd_cbo_auxiliar = models.ForeignKey('profissionais.TabelaCbo', models.DO_NOTHING, db_column='cd_cbo_auxiliar', related_name='atendimento_cd_cbo_auxiliar_set', blank=True, null=True)
    valor_subclassificacao_risco = models.SmallIntegerField(blank=True, null=True, db_column='valor_subclassificacao_risco')
    ds_subclassificacao_risco = models.CharField(max_length=20, blank=True, null=True, db_column='ds_subclassificacao_risco')
    dt_chamada = models.DateTimeField(blank=True, null=True, db_column='dt_chamada')
    cd_profissional_chamada = models.ForeignKey('profissionais.Profissional', models.DO_NOTHING, db_column='cd_profissional_chamada', related_name='atendimento_cd_profissional_chamada_set', blank=True, null=True)
    cd_estabelecimento_cerest = models.ForeignKey('institucional.EstabelecimentoCerest', models.DO_NOTHING, db_column='cd_estabelecimento_cerest', blank=True, null=True)
    flag_permite_reclassificacao = models.SmallIntegerField(blank=True, null=True, db_column='flag_permite_reclassificacao')
    dt_reclassificacao = models.DateTimeField(blank=True, null=True, db_column='dt_reclassificacao')
    dt_canc_lote = models.DateTimeField(blank=True, null=True, db_column='dt_canc_lote')
    flag_consulta = models.SmallIntegerField(blank=True, null=True, db_column='flag_consulta')
    cd_equipe = models.ForeignKey('institucional.Equipe', models.DO_NOTHING, db_column='cd_equipe', blank=True, null=True)
    dt_inicio_agendamento = models.DateTimeField(blank=True, null=True, db_column='dt_inicio_agendamento')
    dt_fim_agendamento = models.DateTimeField(blank=True, null=True, db_column='dt_fim_agendamento')
    flag_preencheu_notificacao = models.SmallIntegerField(blank=True, null=True, db_column='flag_preencheu_notificacao')
    nr_gestas_vaginal = models.SmallIntegerField(blank=True, null=True, db_column='nr_gestas_vaginal')
    nr_gestas_cesariana = models.SmallIntegerField(blank=True, null=True, db_column='nr_gestas_cesariana')
    nr_gestas_aborto = models.SmallIntegerField(blank=True, null=True, db_column='nr_gestas_aborto')
    dt_primeira_usg = models.DateField(blank=True, null=True, db_column='dt_primeira_usg')
    idade_gestacional_usg = models.SmallIntegerField(blank=True, null=True, db_column='idade_gestacional_usg')
    dpp_dum = models.DateField(blank=True, null=True, db_column='dpp_dum')
    dpp_usg = models.DateField(blank=True, null=True, db_column='dpp_usg')
    conduta_covid = models.SmallIntegerField(blank=True, null=True, db_column='conduta_covid')
    cns = models.BigIntegerField(blank=True, null=True, db_column='cns')
    cpf = models.CharField(max_length=11, blank=True, null=True, db_column='cpf')
    motivo_consulta = models.CharField(max_length=50, blank=True, null=True, db_column='motivo_consulta')
    nr_senha = models.IntegerField(blank=True, null=True, db_column='nr_senha')
    tp_senha = models.SmallIntegerField(blank=True, null=True, db_column='tp_senha')
    tipo_participacao_cidadao = models.BigIntegerField(blank=True, null=True, db_column='tipo_participacao_cidadao')

    class Meta:
        managed = False
        db_table = 'atendimento'
        verbose_name = 'Atendimento'
        verbose_name_plural = 'Atendimentos'

    def __str__(self):
        return f"Atendimento {self.nr_atendimento} - {self.nm_paciente or 'Sem Nome'}"
