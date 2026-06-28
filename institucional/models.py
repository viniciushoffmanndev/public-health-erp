from django.db import models
import uuid6


class Empresa(models.Model):
    empresa = models.IntegerField(primary_key=True)
    public_id = models.UUIDField(default=uuid6.uuid7, editable=False, unique=True, db_index=True, db_column='uuid_publico')
    descricao = models.CharField(max_length=60)
    cod_atv = models.ForeignKey('Atividade', models.DO_NOTHING, db_column='cod_atv', blank=True, null=True)
    fantasia = models.CharField(max_length=60, blank=True, null=True)
    rua = models.CharField(max_length=60, blank=True, null=True)
    bairro = models.CharField(max_length=60, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    cod_cid = models.ForeignKey('Cidade', models.DO_NOTHING, db_column='cod_cid')
    cod_pessoa = models.ForeignKey('Pessoa', models.DO_NOTHING, db_column='cod_pessoa', blank=True, null=True, db_comment='Codigo do Cliente')
    fax = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)
    cep = models.CharField(max_length=15, blank=True, null=True)
    contato = models.CharField(max_length=30, blank=True, null=True)
    cnpj = models.CharField(max_length=20, blank=True, null=True)
    inscr_est = models.CharField(max_length=20, blank=True, null=True)
    inscr_mun = models.CharField(max_length=20, blank=True, null=True)
    titulo_janela = models.CharField(max_length=60, blank=True, null=True)
    nome_relatorio = models.CharField(max_length=380, blank=True, null=True)
    sigla = models.CharField(max_length=15, blank=True, null=True, db_comment='Sigla da empresa')
    cd_profissional = models.ForeignKey('Profissional', models.DO_NOTHING, db_column='cd_profissional', blank=True, null=True)
    cnes = models.CharField(max_length=7, blank=True, null=True)
    cnpj_mantenedora = models.ForeignKey('EmpresaMantenedora', models.DO_NOTHING, db_column='cnpj_mantenedora', blank=True, null=True)
    fis_jur = models.CharField(max_length=1, blank=True, null=True)
    cd_siasus = models.CharField(max_length=7, blank=True, null=True)
    reg_saude = models.CharField(max_length=4, blank=True, null=True)
    micro_regiao = models.CharField(max_length=6, blank=True, null=True)
    dist_sanitario = models.CharField(max_length=4, blank=True, null=True)
    dist_admin = models.CharField(max_length=4, blank=True, null=True)
    cd_esfera_admnistrativa = models.ForeignKey('EsferaAdministrativa', models.DO_NOTHING, db_column='cd_esfera_admnistrativa', blank=True, null=True)
    unidade_id_cnes = models.CharField(max_length=31, blank=True, null=True)
    dt_atualizacao = models.DateTimeField(blank=True, null=True)
    cd_hierarquia = models.ForeignKey('NivelHierarquia', models.DO_NOTHING, db_column='cd_hierarquia', blank=True, null=True)
    cd_fluxo_clientela = models.SmallIntegerField(blank=True, null=True)
    ativo = models.CharField(max_length=1, blank=True, null=True)
    dt_inativacao = models.DateTimeField(blank=True, null=True)
    cd_turno_atendimento = models.ForeignKey('TurnoAtendimento', models.DO_NOTHING, db_column='cd_turno_atendimento', blank=True, null=True)
    num_autor_func_anvisa = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    complemento = models.CharField(max_length=60, blank=True, null=True)
    numero = models.CharField(max_length=20, blank=True, null=True)
    tp_controle = models.CharField(max_length=1, blank=True, null=True)
    cd_tp_unidade = models.IntegerField(blank=True, null=True)
    referencia = models.CharField(unique=True, max_length=10, blank=True, null=True)
    version = models.BigIntegerField()
    cd_conta_padrao = models.ForeignKey('Conta', models.DO_NOTHING, db_column='cd_conta_padrao', blank=True, null=True)
    optante_simples = models.CharField(max_length=1, blank=True, null=True)
    numero_pis_pasep = models.CharField(max_length=11, blank=True, null=True)
    caminho_imagem_padrao = models.CharField(blank=True, null=True)
    empresa_princ = models.ForeignKey('self', models.DO_NOTHING, db_column='empresa_princ', blank=True, null=True, related_name='empresa_filhas_set')
    numero_prestador_ipe = models.CharField(max_length=8, blank=True, null=True)
    cd_tipo_prestador_ipe = models.ForeignKey('TipoPrestadorIpe', models.DO_NOTHING, db_column='cd_tipo_prestador_ipe', blank=True, null=True)
    cd_orgao_emissor = models.CharField(max_length=10, blank=True, null=True)
    cd_prof_diretor = models.ForeignKey('Profissional', models.DO_NOTHING, db_column='cd_prof_diretor', related_name='empresa_cd_prof_diretor_set', blank=True, null=True)
    acesso_restrito = models.SmallIntegerField()
    local_atendimento = models.SmallIntegerField(blank=True, null=True)
    dt_integracao_inovamfri = models.DateTimeField(blank=True, null=True)
    flag_integrar = models.SmallIntegerField(blank=True, null=True)
    horario_atendimento = models.CharField(blank=True, null=True)
    cd_cnes_processo = models.ForeignKey('CnesProcesso', models.DO_NOTHING, db_column='cd_cnes_processo', blank=True, null=True)
    flag_exibir_estoque = models.SmallIntegerField(blank=True, null=True)
    rua_adicional = models.CharField(max_length=60, blank=True, null=True)
    numero_adicional = models.CharField(max_length=6, blank=True, null=True)
    bairro_adicional = models.CharField(max_length=60, blank=True, null=True)
    cod_cid_adicional = models.ForeignKey('Cidade', models.DO_NOTHING, db_column='cod_cid_adicional', related_name='empresa_cod_cid_adicional_set', blank=True, null=True)
    cep_adicional = models.CharField(max_length=15, blank=True, null=True)
    consorciado_ativo = models.SmallIntegerField(blank=True, null=True)
    celular = models.CharField(max_length=20, blank=True, null=True)
    vl_manutencao = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    situacao_bloqueio = models.SmallIntegerField()
    dt_bloqueio_ini = models.DateField(blank=True, null=True)
    dt_bloqueio_fim = models.DateField(blank=True, null=True)
    flag_cancelamento_guia = models.SmallIntegerField(blank=True, null=True)
    cd_end_estruturado_distrito = models.ForeignKey('EndEstruturadoDistrito', models.DO_NOTHING, db_column='cd_end_estruturado_distrito', blank=True, null=True)
    id_integracao_terceiro = models.BigIntegerField(blank=True, null=True)
    nm_integracao_terceiro = models.CharField(blank=True, null=True)
    cd_usuario_responsavel = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='cd_usuario_responsavel', blank=True, null=True)
    flag_gera_producao_vacinal_esus = models.SmallIntegerField(blank=True, null=True)
    version_all = models.BigIntegerField(blank=True, null=True)
    flag_visualiza_agenda_outras_unidades = models.SmallIntegerField(blank=True, null=True)
    cd_microrregiao = models.ForeignKey('Microrregiao', models.DO_NOTHING, db_column='cd_microrregiao', blank=True, null=True)
    flag_lista_medicamento_publico = models.SmallIntegerField(blank=True, null=True)
    id_unidade_orcamentaria = models.CharField(max_length=19, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empresa'
        db_table_comment = 'Tabela de Empresas'

    def __str__(self):
        return f"{self.empresa} - {self.fantasia or self.descricao}"


class Equipe(models.Model):
    cd_equipe = models.BigIntegerField(primary_key=True)
    public_id = models.UUIDField(default=uuid6.uuid7, editable=False, unique=True, db_index=True, db_column='uuid_publico')
    seq_equipe = models.IntegerField(blank=True, null=True)
    cd_tp_equipe = models.ForeignKey('TipoEquipe', models.DO_NOTHING, db_column='cd_tp_equipe', blank=True, null=True)
    empresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='empresa', blank=True, null=True)
    nm_referencia = models.CharField(max_length=60, blank=True, null=True)
    dt_ativacao = models.DateField(blank=True, null=True)
    dt_desativacao = models.DateField(blank=True, null=True)
    tp_pop_quilombo = models.CharField(max_length=1, blank=True, null=True, db_comment='1- SIM, 2 - NAO')
    tp_pop_assentado = models.CharField(max_length=1, blank=True, null=True, db_comment='1- SIM, 2 - NAO')
    tp_pop_geral = models.CharField(max_length=1, blank=True, null=True, db_comment='1- SIM, 2 - NAO')
    tp_pop_escola = models.CharField(max_length=1, blank=True, null=True, db_comment='PSE - 1- SIM, 2 - NAO')
    tp_pop_pronasci = models.CharField(max_length=1, blank=True, null=True, db_comment='1- SIM, 2 - NAO')
    tp_pop_indigena = models.CharField(max_length=1, blank=True, null=True, db_comment='1- SIM, 2 - NAO')
    dt_atualizacao = models.DateTimeField(blank=True, null=True)
    tp_desativacao = models.CharField(max_length=2, blank=True, null=True, db_comment='1 - TEMPORARIA, 2 - DEFINITIVA')
    cd_mot_desativacao = models.ForeignKey('MotivoDesativacao', models.DO_NOTHING, db_column='cd_mot_desativacao', blank=True, null=True)
    ativo = models.CharField(max_length=1, blank=True, null=True)
    dt_inativacao = models.DateTimeField(blank=True, null=True)
    version = models.BigIntegerField()
    version_all = models.BigIntegerField(unique=True)
    cd_equipe_cnes = models.CharField(max_length=10, blank=True, null=True)
    cd_equipe_area = models.ForeignKey('EquipeArea', models.DO_NOTHING, db_column='cd_equipe_area')
    permite_alt_paciente = models.SmallIntegerField(blank=True, null=True)
    cd_cnes_processo = models.ForeignKey('CnesProcesso', models.DO_NOTHING, db_column='cd_cnes_processo', blank=True, null=True)
    atendimento_nasfs = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equipe'
        db_table_comment = 'CNES - LFCES037'

    def __str__(self):
        return f"{self.cd_equipe_cnes or self.cd_equipe} - {self.nm_referencia}"


class EstabelecimentoCerest(models.Model):
    cd_estabelecimento_cerest = models.BigIntegerField(primary_key=True)
    public_id = models.UUIDField(default=uuid6.uuid7, editable=False, unique=True, db_index=True, db_column='uuid_publico')
    razao_social = models.CharField(max_length=100)
    fantasia = models.CharField(max_length=50, blank=True, null=True)
    cnpj = models.CharField(max_length=15)
    matriz = models.SmallIntegerField()
    dt_inicio_funcionamento = models.DateField(blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    logradouro = models.CharField(max_length=100, blank=True, null=True)
    nr_logradouro = models.CharField(max_length=6, blank=True, null=True)
    bairro = models.CharField(max_length=100, blank=True, null=True)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    cep = models.CharField(max_length=10, blank=True, null=True)
    cod_cid = models.ForeignKey('Cidade', models.DO_NOTHING, db_column='cod_cid', blank=True, null=True)
    cod_est = models.ForeignKey('Estado', models.DO_NOTHING, db_column='cod_est', blank=True, null=True)
    situacao = models.SmallIntegerField()
    dt_cadastro = models.DateTimeField()
    cd_usuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='cd_usuario')
    dt_cancelamento = models.DateTimeField(blank=True, null=True)
    cd_usuario_can = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='cd_usuario_can', related_name='estabelecimentocerest_cd_usuario_can_set', blank=True, null=True)
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'estabelecimento_cerest'

    def __str__(self):
        return self.fantasia or self.razao_social


class CentroCusto(models.Model):
    cod_centro_custo = models.BigIntegerField(primary_key=True)
    public_id = models.UUIDField(default=uuid6.uuid7, editable=False, unique=True, db_index=True, db_column='uuid_publico')
    descricao = models.CharField(max_length=50)
    mascara = models.CharField(max_length=30, blank=True, null=True)
    empresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='empresa', blank=True, null=True)
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'centro_custo'

    def __str__(self):
        return f"{self.mascara} - {self.descricao}"


class Modulo(models.Model):
    cd_modulo = models.DecimalField(primary_key=True, max_digits=6, decimal_places=0)
    public_id = models.UUIDField(default=uuid6.uuid7, editable=False, unique=True, db_index=True, db_column='uuid_publico')
    nm_modulo = models.CharField(max_length=35)
    rotulo = models.CharField(max_length=50, blank=True, null=True)
    imagem = models.CharField(blank=True, null=True)
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'modulo'
        db_table_comment = 'Módulos do Sistema'

    def __str__(self):
        return self.nm_modulo


# =====================================================================
# STUBS TEMPORÁRIOS PARA ESTE APP
# =====================================================================
class Atividade(models.Model):
    class Meta: 
        managed = False
        db_table = 'atividade'

class Cidade(models.Model):
    class Meta: 
        managed = False
        db_table = 'cidade'

class Pessoa(models.Model):
    class Meta: 
        managed = False
        db_table = 'pessoa'

class Profissional(models.Model):
    class Meta: 
        managed = False
        db_table = 'profissional'

class EmpresaMantenedora(models.Model):
    class Meta: 
        managed = False
        db_table = 'empresa_mantenedora'

class EsferaAdministrativa(models.Model):
    class Meta: 
        managed = False
        db_table = 'esfera_administrativa'

class NivelHierarquia(models.Model):
    class Meta: 
        managed = False
        db_table = 'nivel_hierarquia'

class TurnoAtendimento(models.Model):
    class Meta: 
        managed = False
        db_table = 'turno_atendimento'

class Conta(models.Model):
    class Meta: 
        managed = False
        db_table = 'conta'

class TipoPrestadorIpe(models.Model):
    class Meta: 
        managed = False
        db_table = 'tipo_prestador_ipe'

class CnesProcesso(models.Model):
    class Meta: 
        managed = False
        db_table = 'cnes_processo'

class EndEstruturadoDistrito(models.Model):
    class Meta: 
        managed = False
        db_table = 'end_estruturado_distrito'

class Usuarios(models.Model):
    class Meta: 
        managed = False
        db_table = 'usuarios'

class Microrregiao(models.Model):
    class Meta: 
        managed = False
        db_table = 'microrregiao'

class TipoEquipe(models.Model):
    class Meta: 
        managed = False
        db_table = 'tipo_equipe'

class MotivoDesativacao(models.Model):
    class Meta: 
        managed = False
        db_table = 'motivo_desativacao'

class EquipeArea(models.Model):
    class Meta: 
        managed = False
        db_table = 'equipe_area'

class Estado(models.Model):
    class Meta: 
        managed = False
        db_table = 'estado'