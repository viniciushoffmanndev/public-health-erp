from django.db import models
import uuid6

class Pessoa(models.Model):
    cod_pessoa = models.BigIntegerField(primary_key=True, db_comment='Codigo do Cliente')
    public_id = models.UUIDField(default=uuid6.uuid7, editable=False, unique=True, db_index=True,db_column='uuid_publico')
    descricao = models.CharField(max_length=80, db_comment='Descricao do Cliente')
    fantasia = models.CharField(max_length=30, blank=True, null=True)
    fis_jur = models.CharField(max_length=1)
    cnpj_cpf = models.CharField(max_length=20, blank=True, null=True)
    inscr_est = models.CharField(max_length=20, blank=True, null=True)
    cod_atv = models.ForeignKey('Atividade', models.DO_NOTHING, db_column='cod_atv', blank=True, null=True)
    cod_tip_pessoa = models.ForeignKey('TipoPessoa', models.DO_NOTHING, db_column='cod_tip_pessoa', db_comment='Tabela que identifica o tipo de cliente e fornecedor. Ex: Cliente Ceramica.; Fornecedor de Transporte.')
    flag = models.CharField(max_length=1)
    observacao = models.CharField(max_length=250, blank=True, null=True)
    dt_cadastro = models.DateField()
    descricao_cliente_ant = models.CharField(max_length=80, blank=True, null=True)
    dt_alt_descricao = models.DateField(blank=True, null=True)
    usuario = models.IntegerField()
    dt_usuario = models.DateField()
    cod_representante = models.ForeignKey('self', models.DO_NOTHING, db_column='cod_representante', blank=True, null=True, db_comment='Codigo do representante')
    cliente = models.CharField(max_length=1, blank=True, null=True, db_comment='Se a pessoa é um cliente')
    fornecedor = models.CharField(max_length=1, blank=True, null=True, db_comment='Indica se a pessoa é um fornecedor')
    funcionario = models.CharField(max_length=1, blank=True, null=True, db_comment='Indica se a pessoa é um funcionario')
    representante = models.CharField(max_length=1, blank=True, null=True, db_comment='Indica se a pessoa é um representante')
    possui_seguro = models.CharField(max_length=1, blank=True, null=True)
    ds_seguradora = models.CharField(max_length=40, blank=True, null=True)
    sexo = models.CharField(max_length=1, blank=True, null=True)
    rg = models.CharField(max_length=18, blank=True, null=True)
    princ_prod_comercializados = models.CharField(max_length=200, blank=True, null=True)
    ds_pai = models.CharField(max_length=40, blank=True, null=True)
    ds_mae = models.CharField(max_length=40, blank=True, null=True)
    estado_civil = models.CharField(max_length=1, blank=True, null=True)
    nm_dependentes = models.IntegerField(blank=True, null=True)
    ds_conjuge = models.CharField(max_length=40, blank=True, null=True)
    dt_nascimento_conjuge = models.DateField(blank=True, null=True)
    dt_nascimento = models.DateField(blank=True, null=True)
    associado = models.CharField(max_length=1, blank=True, null=True, db_comment='dado especifico cooperja')
    interno_externo = models.CharField(max_length=1, blank=True, null=True, db_comment='Indica se o cliente e um interno ou externo para algumas validações.')
    ds_marcacao_exportacao = models.CharField(max_length=200, blank=True, null=True)
    nr_comissao_armador = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    perc_comissao = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    cta_contabil = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    version = models.BigIntegerField()
    num_contrato = models.CharField(max_length=20, blank=True, null=True)
    dt_contrato = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pessoa'
        db_table_comment = 'Aqui ficará registrado os dados das pessoas'


class UsuarioCadsus(models.Model):
    cd_usu_cadsus = models.DecimalField(primary_key=True, max_digits=8, decimal_places=0)
    #public_id = models.UUIDField(default=uuid6.uuid7, editable=False, unique=True, db_index=True,db_column='uuid_publico')
    nm_usuario = models.CharField(max_length=70)
    sg_sexo = models.CharField(max_length=1)
    nm_mae = models.CharField(max_length=70, blank=True, null=True)
    nm_pai = models.CharField(max_length=70, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    cod_cid_nascimento = models.ForeignKey('geografia.Cidade', models.DO_NOTHING, db_column='cod_cid_nascimento', blank=True, null=True)
    cpf = models.CharField(max_length=14, blank=True, null=True)
    rg = models.CharField(max_length=20, blank=True, null=True)
    dt_nascimento = models.DateField()
    cd_pais_nascimento = models.ForeignKey('Nacionalidade', models.DO_NOTHING, db_column='cd_pais_nascimento', blank=True, null=True)
    st_profissional = models.SmallIntegerField(blank=True, null=True)
    st_frequenta_escola = models.CharField(max_length=1, blank=True, null=True)
    cd_raca = models.ForeignKey('Raca', models.DO_NOTHING, db_column='cd_raca', blank=True, null=True)
    cd_estado_civil = models.ForeignKey('EstadoCivil', models.DO_NOTHING, db_column='cd_estado_civil', blank=True, null=True)
    cd_situacao_familiar = models.SmallIntegerField(blank=True, null=True)
    cd_cbo = models.ForeignKey('profissionais.TabelaCbo', models.DO_NOTHING, db_column='cd_cbo', blank=True, null=True)
    nr_telefone = models.CharField(max_length=15, blank=True, null=True)
    nr_telefone_2 = models.CharField(max_length=15, blank=True, null=True)
    dt_inclusao = models.DateField()
    dt_preenchimento_form = models.DateField()
    cd_municipio_residencia = models.ForeignKey('geografia.Cidade', models.DO_NOTHING, db_column='cd_municipio_residencia', related_name='usuariocadsus_cd_municipio_residencia_set', blank=True, null=True)
    st_sem_documento = models.SmallIntegerField(blank=True, null=True)
    nr_usuario_no_domicilio = models.SmallIntegerField(blank=True, null=True)
    st_vivo = models.SmallIntegerField(blank=True, null=True)
    cd_usuario_interno = models.CharField(max_length=60, blank=True, null=True)
    st_excluido = models.SmallIntegerField()
    cd_domicilio_interno = models.CharField(max_length=50, blank=True, null=True)
    cd_domicilio = models.BigIntegerField(blank=True, null=True)
    cd_escolaridade = models.ForeignKey('Escolaridade', models.DO_NOTHING, db_column='cd_escolaridade', blank=True, null=True)
    dt_alteracao = models.DateTimeField(blank=True, null=True)
    empresa_responsavel = models.ForeignKey('institucional.Empresa', models.DO_NOTHING, db_column='empresa_responsavel', blank=True, null=True)
    situacao = models.SmallIntegerField(blank=True, null=True)
    dt_inativacao = models.DateTimeField(blank=True, null=True)
    dt_fixacao = models.DateField(blank=True, null=True)
    st_aprovacao = models.SmallIntegerField(blank=True, null=True)
    dt_aprovacao = models.DateTimeField(blank=True, null=True)
    flag_documento = models.CharField(max_length=1, blank=True, null=True)
    dt_cadastro = models.DateTimeField(blank=True, null=True)
    celular = models.CharField(max_length=15, blank=True, null=True)
    telefone3 = models.CharField(max_length=15, blank=True, null=True)
    telefone4 = models.CharField(max_length=15, blank=True, null=True)
    externo = models.CharField(max_length=1, blank=True, null=True)
    version = models.BigIntegerField()
    dt_usuario = models.DateTimeField()
    cd_usuario = models.ForeignKey('profissionais.Usuarios', models.DO_NOTHING, db_column='cd_usuario')
    observacao = models.CharField(max_length=1024, blank=True, null=True)
    religiao = models.CharField(max_length=50, blank=True, null=True)
    local_trabalho = models.CharField(max_length=50, blank=True, null=True)
    telefone_trabalho = models.CharField(max_length=15, blank=True, null=True)
    responsavel = models.CharField(max_length=70, blank=True, null=True)
    parentesco_responsavel = models.CharField(max_length=20, blank=True, null=True)
    urgencia_chamar = models.CharField(max_length=70, blank=True, null=True)
    telefone_urgencia = models.CharField(max_length=15, blank=True, null=True)
    grau_parentesco_urgencia = models.CharField(max_length=20, blank=True, null=True)
    recem_nascido = models.CharField(max_length=1, blank=True, null=True)
    nome_conjuge = models.CharField(max_length=70, blank=True, null=True)
    flag_simplificado = models.SmallIntegerField(blank=True, null=True)
    flag_estrangeiro = models.SmallIntegerField(blank=True, null=True)
    flag_nao_possui_cns = models.SmallIntegerField(blank=True, null=True)
    cd_local_permanencia = models.ForeignKey('LocalPermanencia', models.DO_NOTHING, db_column='cd_local_permanencia', blank=True, null=True)
    nr_atendimento_origem = models.ForeignKey('atendimentos.Atendimento', models.DO_NOTHING, db_column='nr_atendimento_origem', blank=True, null=True)
    chave_biometria = models.TextField(blank=True, null=True)
    cd_endereco = models.ForeignKey('geografia.EnderecoUsuarioCadsus', models.DO_NOTHING, db_column='cd_endereco', blank=True, null=True)
    nacionalidade = models.SmallIntegerField(blank=True, null=True)
    apelido = models.CharField(max_length=50, blank=True, null=True)
    flag_responsavel_familiar = models.SmallIntegerField(blank=True, null=True)
    cd_usu_cadsus_responsavel = models.ForeignKey('self', models.DO_NOTHING, db_column='cd_usu_cadsus_responsavel', blank=True, null=True)
    version_all = models.BigIntegerField(unique=True)
    renda_familiar = models.IntegerField(blank=True, null=True)
    reside_desde = models.DateField(blank=True, null=True)
    nis = models.CharField(blank=True, null=True)
    flag_recem_nascido_recepcao = models.CharField(max_length=1, blank=True, null=True)
    mot_exclusao = models.SmallIntegerField(blank=True, null=True)
    prontuario = models.CharField(max_length=30, blank=True, null=True)
    cd_etnia = models.ForeignKey('EtniaIndigena', models.DO_NOTHING, db_column='cd_etnia', blank=True, null=True)
    cd_gerenciador_arquivo = models.ForeignKey('GerenciadorArquivo', models.DO_NOTHING, db_column='cd_gerenciador_arquivo', blank=True, null=True)
    tipo_sanguineo = models.SmallIntegerField(blank=True, null=True)
    referencia = models.CharField(unique=True, max_length=10, blank=True, null=True)
    uuid_tablet = models.CharField(blank=True, null=True)
    profissao = models.CharField(max_length=50, blank=True, null=True)
    cd_estabelecimento_cerest = models.ForeignKey('institucional.EstabelecimentoCerest', models.DO_NOTHING, db_column='cd_estabelecimento_cerest', blank=True, null=True)
    cd_usuario_cad = models.ForeignKey('profissionais.Usuarios', models.DO_NOTHING, db_column='cd_usuario_cad', related_name='usuariocadsus_cd_usuario_cad_set')
    flag_utiliza_nome_social = models.SmallIntegerField()
    cd_usu_cadsus_unificado = models.ForeignKey('self', models.DO_NOTHING, db_column='cd_usu_cadsus_unificado', related_name='usuariocadsus_cd_usu_cadsus_unificado_set', blank=True, null=True)
    flag_unificado = models.SmallIntegerField()
    responsavel_anterior = models.SmallIntegerField(blank=True, null=True)
    cd_equipe = models.ForeignKey('institucional.Equipe', models.DO_NOTHING, db_column='cd_equipe', blank=True, null=True)
    flag_outras_pop_nomades = models.SmallIntegerField()
    nivel_escolaridade = models.SmallIntegerField(blank=True, null=True)
    beneficiario_bolsa_familia = models.SmallIntegerField(blank=True, null=True)
    app_cidadao_ativo = models.BooleanField(blank=True, null=True)
    grupo_vacinacao = models.BigIntegerField(blank=True, null=True)
    dt_alteracao_app = models.DateTimeField(blank=True, null=True)
    cd_equipe_profissional = models.ForeignKey('EquipeProfissional', models.DO_NOTHING, db_column='cd_equipe_profissional', blank=True, null=True)
    flag_nao_possui_cpf = models.SmallIntegerField(blank=True, null=True)
    cd_comunidade = models.ForeignKey('ComunidadeTradicional', models.DO_NOTHING, db_column='cd_comunidade', blank=True, null=True)
    cd_motivo_cpf = models.ForeignKey('UsuarioCadsusMotivoCpf', models.DO_NOTHING, db_column='cd_motivo_cpf', blank=True, null=True)
    flag_visivel_prontuario = models.SmallIntegerField(blank=True, null=True)
    cd_equipe_vinculo = models.ForeignKey('institucional.Equipe', models.DO_NOTHING, db_column='cd_equipe_vinculo', related_name='usuariocadsus_cd_equipe_vinculo_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario_cadsus'


class UsuarioCadsusHistorico(models.Model):
    cd_usu_cadsus = models.ForeignKey(UsuarioCadsus, models.DO_NOTHING, db_column='cd_usu_cadsus', primary_key=True)
    dt_alteracao = models.DateTimeField()
    empresa = models.ForeignKey('institucional.Empresa', models.DO_NOTHING, db_column='empresa')
    cd_usuario = models.ForeignKey('profissionais.Usuarios', models.DO_NOTHING, db_column='cd_usuario')
    tipo = models.CharField(max_length=1, db_comment='I-Inclusao, A-Alteracao, E-Exclusao.')
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'usuario_cadsus_historico'
        unique_together = (('cd_usu_cadsus', 'dt_alteracao'),)


# =====================================================================
# STUBS SECUNDÁRIOS RESTANTES (Proteção Final)
# =====================================================================
class Atividade(models.Model): 
    class Meta: 
        managed=False
        db_table='atividade'
class TipoPessoa(models.Model): 
    class Meta: 
        managed=False
        db_table='tipo_pessoa'
class Nacionalidade(models.Model): 
    class Meta: 
        managed=False
        db_table='nacionalidade'
class Raca(models.Model): 
    class Meta: 
        managed=False
        db_table='raca'
class EstadoCivil(models.Model):
    class Meta: 
        managed=False
        db_table='estado_civil'
class Escolaridade(models.Model): 
    class Meta: 
        managed=False
        db_table='escolaridade'
class LocalPermanencia(models.Model): 
    class Meta: 
        managed=False
        db_table='local_permanencia'
class EtniaIndigena(models.Model): 
    class Meta: 
        managed=False
        db_table='etnia_indigena'
class GerenciadorArquivo(models.Model): 
    class Meta: 
        managed=False
        db_table='gerenciador_arquivo'
class EquipeProfissional(models.Model): 
    class Meta: 
        managed=False
        db_table='equipe_profissional'
class ComunidadeTradicional(models.Model): 
    class Meta: 
        managed=False
        db_table='comunidade_tradicional'
class UsuarioCadsusMotivoCpf(models.Model): 
    class Meta: 
        managed=False
        db_table='usuario_cadsus_motivo_cpf'