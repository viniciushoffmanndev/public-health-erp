from django.db import models
import uuid6


class Atividade(models.Model): 
    class Meta: 
        managed=False
        db_table='atividade'

    def __str__(self):
        return f"Atividade {self.pk}"


class TipoPessoa(models.Model):
    cod_tip_pessoa = models.IntegerField(primary_key=True, db_column='cod_tip_pessoa')
    descricao = models.CharField(max_length=40, db_column='descricao')
    sigla =  models.CharField(max_length=10, db_column='sigla')
    version = models.BigIntegerField(db_column='version')

    class Meta:
        managed = False
        db_table = 'tipo_pessoa'
        verbose_name = 'Tipo de Pessoa'
        verbose_name_plural = 'Tipos de Pessoa'

    def __str__(self):
        return f"{self.sigla} - {self.descricao}"


class Nacionalidade(models.Model): 
    cd_pais = models.IntegerField(primary_key=True, db_column='cd_pais')
    ds_pais = models.CharField(max_length=150, db_column='ds_pais')
    version = models.BigIntegerField(db_column='version')
    version_all = models.BigIntegerField(db_column='version_all')
    cd_pni = models.IntegerField(blank=True, null=True, db_column='cd_pni')
    cd_esus = models.BigIntegerField(blank=True, null=True, db_column='cd_esus')

    class Meta: 
        managed = False
        db_table = 'nacionalidade'
        verbose_name = 'Nacionalidade'
        verbose_name_plural = 'Nacionalidades'

    def __str__(self):
        return f"{self.cd_pais} - {self.ds_pais}"


class Raca(models.Model): 
    cd_raca = models.SmallIntegerField(primary_key=True, db_column='cd_raca')
    ds_raca = models.CharField(max_length=30, db_column='ds_raca')  # Alterado cirurgicamente para 30!
    version = models.BigIntegerField(db_column='version')
    version_all = models.BigIntegerField(db_column='version_all')

    class Meta: 
        managed = False
        db_table = 'raca'
        verbose_name = 'Raça / Cor'
        verbose_name_plural = 'Raças / Cores'

    def __str__(self):
        return f"{self.cd_raca} - {self.ds_raca}"


class EstadoCivil(models.Model):
    class Meta: 
        managed=False
        db_table='estado_civil'

    def __str__(self):
        return f"Estado Civil {self.pk}"


class Escolaridade(models.Model): 
    class Meta: 
        managed=False
        db_table='escolaridade'

    def __str__(self):
        return f"Escolaridade {self.pk}"


class LocalPermanencia(models.Model): 
    class Meta: 
        managed=False
        db_table='local_permanencia'

    def __str__(self):
        return f"Local Permanência {self.pk}"


class EtniaIndigena(models.Model): 
    class Meta: 
        managed=False
        db_table='etnia_indigena'

    def __str__(self):
        return f"Etnia Indígena {self.pk}"
    

class GerenciadorArquivo(models.Model): 
    class Meta: 
        managed=False
        db_table='gerenciador_arquivo'
    
    def __str__(self):
        return f"Gerenciador Arquivo {self.pk}"
    

class EquipeProfissional(models.Model): 
    class Meta: 
        managed=False
        db_table='equipe_profissional'

    def __str__(self):
        return f"Equipe Profissional {self.pk}"


class ComunidadeTradicional(models.Model): 
    class Meta: 
        managed=False
        db_table='comunidade_tradicional'

    def __str__(self):
        return f"Comunidade Tradicional {self.pk}"


class UsuarioCadsusMotivoCpf(models.Model):
    class Meta: 
        managed=False
        db_table='usuario_cadsus_motivo_cpf'

    def __str__(self):
        return f"Motivo CPF {self.pk}"


class Pessoa(models.Model):
    cod_pessoa = models.BigIntegerField(primary_key=True, db_column='cod_pessoa')
   # public_id = models.UUIDField(default=uuid6.uuid7, editable=False, unique=True, db_index=True, db_column='uuid_publico')
    descricao = models.CharField(max_length=80, db_column='descricao')
    fantasia = models.CharField(max_length=30, blank=True, null=True, db_column='fantasia')
    fis_jur = models.CharField(max_length=1, db_column='fis_jur')
    cnpj_cpf = models.CharField(max_length=20, blank=True, null=True, db_column='cnpj_cpf')
    inscr_est = models.CharField(max_length=20, blank=True, null=True, db_column='inscr_est')
    cod_atv = models.ForeignKey('Atividade', models.DO_NOTHING, db_column='cod_atv', blank=True, null=True)
    cod_tip_pessoa = models.ForeignKey('TipoPessoa', models.DO_NOTHING, db_column='cod_tip_pessoa')
    flag = models.CharField(max_length=1, db_column='flag')
    observacao = models.CharField(max_length=250, blank=True, null=True, db_column='observacao')
    dt_cadastro = models.DateField(db_column='dt_cadastro')
    descricao_cliente_ant = models.CharField(max_length=80, blank=True, null=True, db_column='descricao_cliente_ant')
    dt_alt_descricao = models.DateField(blank=True, null=True, db_column='dt_alt_descricao')
    usuario = models.IntegerField(db_column='usuario')
    dt_usuario = models.DateField(db_column='dt_usuario')
    cod_representante = models.ForeignKey('self', models.DO_NOTHING, db_column='cod_representante', blank=True, null=True)
    cliente = models.CharField(max_length=1, blank=True, null=True, db_column='cliente')
    fornecedor = models.CharField(max_length=1, blank=True, null=True, db_column='fornecedor')
    funcionario = models.CharField(max_length=1, blank=True, null=True, db_column='funcionario')
    representante = models.CharField(max_length=1, blank=True, null=True, db_column='representante')
    possui_seguro = models.CharField(max_length=1, blank=True, null=True, db_column='possui_seguro')
    ds_seguradora = models.CharField(max_length=40, blank=True, null=True, db_column='ds_seguradora')
    sexo = models.CharField(max_length=1, blank=True, null=True, db_column='sexo')
    rg = models.CharField(max_length=18, blank=True, null=True, db_column='rg')
    princ_prod_comercializados = models.CharField(max_length=200, blank=True, null=True, db_column='princ_prod_comercializados')
    ds_pai = models.CharField(max_length=40, blank=True, null=True, db_column='ds_pai')
    ds_mae = models.CharField(max_length=40, blank=True, null=True, db_column='ds_mae')
    estado_civil = models.CharField(max_length=1, blank=True, null=True, db_column='estado_civil')
    nm_dependentes = models.IntegerField(blank=True, null=True, db_column='nm_dependentes')
    ds_conjuge = models.CharField(max_length=40, blank=True, null=True, db_column='ds_conjuge')
    dt_nascimento_conjuge = models.DateField(blank=True, null=True, db_column='dt_nascimento_conjuge')
    dt_nascimento = models.DateField(blank=True, null=True, db_column='dt_nascimento')
    associado = models.CharField(max_length=1, blank=True, null=True, db_column='associado')
    interno_externo = models.CharField(max_length=1, blank=True, null=True, db_column='interno_externo')
    ds_marcacao_exportacao = models.CharField(max_length=200, blank=True, null=True, db_column='ds_marcacao_exportacao')
    nr_comissao_armador = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True, db_column='nr_comissao_armador')
    perc_comissao = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, db_column='perc_comissao')
    cta_contabil = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True, db_column='cta_contabil')
    version = models.BigIntegerField(db_column='version')
    num_contrato = models.CharField(max_length=20, blank=True, null=True, db_column='num_contrato')
    dt_contrato = models.DateField(blank=True, null=True, db_column='dt_contrato')

    class Meta:
        managed = False
        db_table = 'pessoa'
        verbose_name = 'Pessoa (Cadastro Geral)'
        verbose_name_plural = 'Pessoas (Cadastro Geral)'

    def __str__(self):
        return f"{self.cod_pessoa} - {self.descricao}"


class UsuarioCadsus(models.Model):
    # Ajustado de DecimalField para BigIntegerField baseado no tipo 'numeric' do banco
    cd_usu_cadsus = models.BigIntegerField(primary_key=True, db_column='cd_usu_cadsus')
    nm_usuario = models.CharField(max_length=70, db_column='nm_usuario')
    sg_sexo = models.CharField(max_length=1, db_column='sg_sexo')
    nm_mae = models.CharField(max_length=70, blank=True, null=True, db_column='nm_mae')
    nm_pai = models.CharField(max_length=70, blank=True, null=True, db_column='nm_pai')
    email = models.CharField(max_length=100, blank=True, null=True, db_column='email')
    cod_cid_nascimento = models.ForeignKey('geografia.Cidade', models.DO_NOTHING, db_column='cod_cid_nascimento', blank=True, null=True)
    cpf = models.CharField(max_length=14, blank=True, null=True, db_column='cpf')
    rg = models.CharField(max_length=20, blank=True, null=True, db_column='rg')
    dt_nascimento = models.DateField(db_column='dt_nascimento')
    cd_pais_nascimento = models.ForeignKey('Nacionalidade', models.DO_NOTHING, db_column='cd_pais_nascimento', blank=True, null=True)
    st_profissional = models.SmallIntegerField(blank=True, null=True, db_column='st_profissional')
    st_frequenta_escola = models.CharField(max_length=1, blank=True, null=True, db_column='st_frequenta_escola')
    cd_raca = models.ForeignKey('Raca', models.DO_NOTHING, db_column='cd_raca', blank=True, null=True)
    cd_estado_civil = models.ForeignKey('EstadoCivil', models.DO_NOTHING, db_column='cd_estado_civil', blank=True, null=True)
    cd_situacao_familiar = models.SmallIntegerField(blank=True, null=True, db_column='cd_situacao_familiar')
    cd_cbo = models.ForeignKey('profissionais.TabelaCbo', models.DO_NOTHING, db_column='cd_cbo', blank=True, null=True)
    nr_telefone = models.CharField(max_length=15, blank=True, null=True, db_column='nr_telefone')
    nr_telefone_2 = models.CharField(max_length=15, blank=True, null=True, db_column='nr_telefone_2')
    dt_inclusao = models.DateField(db_column='dt_inclusao')
    dt_preenchimento_form = models.DateField(db_column='dt_preenchimento_form')
    cd_municipio_residencia = models.ForeignKey('geografia.Cidade', models.DO_NOTHING, db_column='cd_municipio_residencia', related_name='usuariocadsus_cd_municipio_residencia_set', blank=True, null=True)
    st_sem_documento = models.SmallIntegerField(blank=True, null=True, db_column='st_sem_documento')
    nr_usuario_no_domicilio = models.SmallIntegerField(blank=True, null=True, db_column='nr_usuario_no_domicilio')
    st_vivo = models.SmallIntegerField(blank=True, null=True, db_column='st_vivo')
    cd_usuario_interno = models.CharField(max_length=60, blank=True, null=True, db_column='cd_usuario_interno')
    st_excluido = models.SmallIntegerField(db_column='st_excluido')
    cd_domicilio_interno = models.CharField(max_length=50, blank=True, null=True, db_column='cd_domicilio_interno')
    cd_domicilio = models.BigIntegerField(blank=True, null=True, db_column='cd_domicilio')
    cd_escolaridade = models.ForeignKey('Escolaridade', models.DO_NOTHING, db_column='cd_escolaridade', blank=True, null=True)
    dt_alteracao = models.DateTimeField(blank=True, null=True, db_column='dt_alteracao')
    empresa_responsavel = models.ForeignKey('institucional.Empresa', models.DO_NOTHING, db_column='empresa_responsavel', blank=True, null=True)
    situacao = models.SmallIntegerField(blank=True, null=True, db_column='situacao')
    dt_inativacao = models.DateTimeField(blank=True, null=True, db_column='dt_inativacao')
    dt_fixacao = models.DateField(blank=True, null=True, db_column='dt_fixacao')
    st_aprovacao = models.SmallIntegerField(blank=True, null=True, db_column='st_aprovacao')
    dt_aprovacao = models.DateTimeField(blank=True, null=True, db_column='dt_aprovacao')
    flag_documento = models.CharField(max_length=1, blank=True, null=True, db_column='flag_documento')
    dt_cadastro = models.DateTimeField(blank=True, null=True, db_column='dt_cadastro')
    celular = models.CharField(max_length=15, blank=True, null=True, db_column='celular')
    telefone3 = models.CharField(max_length=15, blank=True, null=True, db_column='telefone3')
    telefone4 = models.CharField(max_length=15, blank=True, null=True, db_column='telefone4')
    externo = models.CharField(max_length=1, blank=True, null=True, db_column='externo')
    version = models.BigIntegerField(db_column='version')
    dt_usuario = models.DateTimeField(db_column='dt_usuario')
    cd_usuario = models.ForeignKey('profissionais.Usuarios', models.DO_NOTHING, db_column='cd_usuario')
    observacao = models.CharField(max_length=1024, blank=True, null=True, db_column='observacao')
    religiao = models.CharField(max_length=50, blank=True, null=True, db_column='religiao')
    local_trabalho = models.CharField(max_length=50, blank=True, null=True, db_column='local_trabalho')
    telefone_trabalho = models.CharField(max_length=15, blank=True, null=True, db_column='telefone_trabalho')
    responsavel = models.CharField(max_length=70, blank=True, null=True, db_column='responsavel')
    parentesco_responsavel = models.CharField(max_length=20, blank=True, null=True, db_column='parentesco_responsavel')
    urgencia_chamar = models.CharField(max_length=70, blank=True, null=True, db_column='urgencia_chamar')
    telefone_urgencia = models.CharField(max_length=15, blank=True, null=True, db_column='telefone_urgencia')
    grau_parentesco_urgencia = models.CharField(max_length=20, blank=True, null=True, db_column='grau_parentesco_urgencia')
    recem_nascido = models.CharField(max_length=1, blank=True, null=True, db_column='recem_nascido')
    nome_conjuge = models.CharField(max_length=70, blank=True, null=True, db_column='nome_conjuge')
    flag_simplificado = models.SmallIntegerField(blank=True, null=True, db_column='flag_simplificado')
    flag_estrangeiro = models.SmallIntegerField(blank=True, null=True, db_column='flag_estrangeiro')
    flag_nao_possui_cns = models.SmallIntegerField(blank=True, null=True, db_column='flag_nao_possui_cns')
    cd_local_permanencia = models.ForeignKey('LocalPermanencia', models.DO_NOTHING, db_column='cd_local_permanencia', blank=True, null=True)
    nr_atendimento_origem = models.ForeignKey('atendimentos.Atendimento', models.DO_NOTHING, db_column='nr_atendimento_origem', blank=True, null=True)
    chave_biometria = models.TextField(blank=True, null=True, db_column='chave_biometria')
    cd_endereco = models.ForeignKey('geografia.EnderecoUsuarioCadsus', models.DO_NOTHING, db_column='cd_endereco', blank=True, null=True)
    nacionalidade = models.SmallIntegerField(blank=True, null=True, db_column='nacionalidade')
    apelido = models.CharField(max_length=50, blank=True, null=True, db_column='apelido')
    flag_responsavel_familiar = models.SmallIntegerField(blank=True, null=True, db_column='flag_responsavel_familiar')
    cd_usu_cadsus_responsavel = models.ForeignKey('self', models.DO_NOTHING, db_column='cd_usu_cadsus_responsavel', blank=True, null=True)
    version_all = models.BigIntegerField(unique=True, db_column='version_all')
    renda_familiar = models.IntegerField(blank=True, null=True, db_column='renda_familiar')
    reside_desde = models.DateField(blank=True, null=True, db_column='reside_desde')
    nis = models.CharField(blank=True, null=True, db_column='nis')
    flag_recem_nascido_recepcao = models.CharField(max_length=1, blank=True, null=True, db_column='flag_recem_nascido_recepcao')
    mot_exclusao = models.SmallIntegerField(blank=True, null=True, db_column='mot_exclusao')
    prontuario = models.CharField(max_length=30, blank=True, null=True, db_column='prontuario')
    cd_etnia = models.ForeignKey('EtniaIndigena', models.DO_NOTHING, db_column='cd_etnia', blank=True, null=True)
    cd_gerenciador_arquivo = models.ForeignKey('GerenciadorArquivo', models.DO_NOTHING, db_column='cd_gerenciador_arquivo', blank=True, null=True)
    tipo_sanguineo = models.SmallIntegerField(blank=True, null=True, db_column='tipo_sanguineo')
    referencia = models.CharField(unique=True, max_length=10, blank=True, null=True, db_column='referencia')
    uuid_tablet = models.CharField(blank=True, null=True, db_column='uuid_tablet')
    profissao = models.CharField(max_length=50, blank=True, null=True, db_column='profissao')
    cd_estabelecimento_cerest = models.ForeignKey('institucional.EstabelecimentoCerest', models.DO_NOTHING, db_column='cd_estabelecimento_cerest', blank=True, null=True)
    cd_usuario_cad = models.ForeignKey('profissionais.Usuarios', models.DO_NOTHING, db_column='cd_usuario_cad', related_name='usuariocadsus_cd_usuario_cad_set')
    flag_utiliza_nome_social = models.SmallIntegerField(default=0, db_column='flag_utiliza_nome_social')
    cd_usu_cadsus_unificado = models.ForeignKey('self', models.DO_NOTHING, db_column='cd_usu_cadsus_unificado', related_name='usuariocadsus_cd_usu_cadsus_unificado_set', blank=True, null=True)
    flag_unificado = models.SmallIntegerField(default=0, db_column='flag_unificado')
    responsavel_anterior = models.SmallIntegerField(blank=True, null=True, db_column='responsavel_anterior')
    cd_equipe = models.ForeignKey('institucional.Equipe', models.DO_NOTHING, db_column='cd_equipe', blank=True, null=True)
    flag_outras_pop_nomades = models.SmallIntegerField(default=0, db_column='flag_outras_pop_nomades')
    nivel_escolaridade = models.SmallIntegerField(blank=True, null=True, db_column='nivel_escolaridade')
    beneficiario_bolsa_familia = models.SmallIntegerField(blank=True, null=True, db_column='beneficiario_bolsa_familia')
    app_cidadao_ativo = models.BooleanField(blank=True, null=True, db_column='app_cidadao_ativo')
    grupo_vacinacao = models.BigIntegerField(blank=True, null=True, db_column='grupo_vacinacao')
    dt_alteracao_app = models.DateTimeField(blank=True, null=True, db_column='dt_alteracao_app')
    cd_equipe_profissional = models.ForeignKey('EquipeProfissional', models.DO_NOTHING, db_column='cd_equipe_profissional', blank=True, null=True)
    flag_nao_possui_cpf = models.SmallIntegerField(blank=True, null=True, db_column='flag_nao_possui_cpf')
    cd_comunidade = models.ForeignKey('ComunidadeTradicional', models.DO_NOTHING, db_column='cd_comunidade', blank=True, null=True)
    cd_motivo_cpf = models.ForeignKey('UsuarioCadsusMotivoCpf', models.DO_NOTHING, db_column='cd_motivo_cpf', blank=True, null=True)
    flag_visivel_prontuario = models.SmallIntegerField(blank=True, null=True, db_column='flag_visivel_prontuario')
    cd_equipe_vinculo = models.ForeignKey('institucional.Equipe', models.DO_NOTHING, db_column='cd_equipe_vinculo', related_name='usuariocadsus_cd_equipe_vinculo_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario_cadsus'
        verbose_name = 'Usuário CADSUS (Paciente)'
        verbose_name_plural = 'Usuários CADSUS (Pacientes)'

    def __str__(self):
        return f"{self.nm_usuario} (Prontuário: {self.prontuario or 'S/P'})"


class UsuarioCadsusHistorico(models.Model):
    cd_usu_cadsus = models.OneToOneField('UsuarioCadsus', models.DO_NOTHING, db_column='cd_usu_cadsus')
    dt_alteracao = models.DateTimeField()
    empresa = models.ForeignKey('institucional.Empresa', models.DO_NOTHING, db_column='empresa')
    cd_usuario = models.ForeignKey('profissionais.Usuarios', models.DO_NOTHING, db_column='cd_usuario')
    tipo = models.CharField(max_length=1, db_comment='I-Inclusao, A-Alteracao, E-Exclusao.')
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'usuario_cadsus_historico'
        unique_together = (('cd_usu_cadsus', 'dt_alteracao'),)