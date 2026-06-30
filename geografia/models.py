from django.db import models
import uuid6


class Cidade(models.Model):
    cod_cid = models.BigIntegerField(primary_key=True)
    public_id = models.UUIDField(default=uuid6.uuid7, editable=False, unique=True, db_index=True, db_column='uuid_publico')
    descricao = models.CharField(max_length=50)
    cod_est = models.ForeignKey('Estado', models.DO_NOTHING, db_column='cod_est')
    version = models.BigIntegerField()
    version_all = models.BigIntegerField(unique=True)
    cd_esus = models.BigIntegerField(blank=True, null=True)
    flag_liberar_disp = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cidade'
        db_table_comment = 'Tabela de Cidades'

    def __str__(self):
        return self.descricao


class EnderecoDomicilio(models.Model):
    cd_domicilio = models.BigIntegerField(primary_key=True)
    public_id = models.UUIDField(default=uuid6.uuid7, editable=False, unique=True, db_index=True, db_column='uuid_publico')
    cd_cadastrador = models.IntegerField(blank=True, null=True)
    nr_ficha = models.IntegerField(blank=True, null=True)
    nr_domicilio = models.CharField(max_length=16, blank=True, null=True)
    ds_uso_municipal = models.CharField(max_length=200, blank=True, null=True)
    qt_pessoas = models.SmallIntegerField(blank=True, null=True)
    cd_programas_cobertura = models.SmallIntegerField(blank=True, null=True, db_comment='1 = PACS; 2 = PSF; 3 = Outros; 4 = Similares PSF')
    qt_comodos = models.SmallIntegerField(blank=True, null=True)
    cd_esgoto_sanitario = models.SmallIntegerField(blank=True, null=True, db_comment='1 = Rede Pública de Esgoto; 2 = Fossa; 3 = Esgoto a céu aberto; X = Inválido')
    cd_tipo_domicilio = models.SmallIntegerField(blank=True, null=True, db_comment='1 = Tijolo; 2 = Taipa revestida; 3 = Taipa não revestida; 4 = Madeira; 5 = Material aproveitado; 6 = Outro; 7 = Adobe; X = Inválido')
    cd_destino_lixo = models.SmallIntegerField(blank=True, null=True, db_comment='1 = Coletado; 2 = Queimado; 3 = Céu aberto; X = Inválido')
    cd_abastecimento_agua = models.SmallIntegerField(blank=True, null=True, db_comment='1 = Rede Pública; 2 = Poço; 3 = Outros; X = Inválido')
    cd_tratamento_agua = models.SmallIntegerField(blank=True, null=True, db_comment='1 = Filtrada; 2 = Fervida; 3 = Clorada; 4 = Sem tratamento; X = Inválido')
    st_energia_eletrica = models.SmallIntegerField(blank=True, null=True, db_comment='0 = não; 1 = sim;')
    cod_cid = models.ForeignKey(Cidade, models.DO_NOTHING, db_column='cod_cid', blank=True, null=True)
    dt_preenchimento = models.DateField(blank=True, null=True)
    nr_segmento = models.SmallIntegerField(blank=True, null=True)
    nr_area = models.SmallIntegerField(blank=True, null=True)
    nr_micro_area = models.SmallIntegerField(blank=True, null=True)
    nr_familia = models.BigIntegerField(blank=True, null=True)
    nr_latitude = models.CharField(max_length=10, blank=True, null=True)
    nr_longitude = models.CharField(max_length=10, blank=True, null=True)
    st_excluido = models.SmallIntegerField(db_comment='0 = ativo; 1 = excluído.')
    cd_domicilio_interno = models.CharField(max_length=50, blank=True, null=True, db_comment='codigo do domicilio dentro do cadsus (integrador)')
    cd_endereco = models.ForeignKey('EnderecoUsuarioCadsus', models.DO_NOTHING, db_column='cd_endereco')
    cd_profissional = models.ForeignKey('profissionais.Profissional', models.DO_NOTHING, db_column='cd_profissional', blank=True, null=True)
    dt_alteracao = models.DateTimeField(blank=True, null=True)
    possui_plano = models.CharField(max_length=1, blank=True, null=True)
    nr_pessoa_coberta_plano = models.IntegerField(blank=True, null=True)
    nm_plano_saude = models.CharField(max_length=100, blank=True, null=True)
    cd_procura_doenca = models.SmallIntegerField(blank=True, null=True)
    ds_outros_procura_doenca = models.CharField(max_length=50, blank=True, null=True)
    cd_meio_comunicacao = models.SmallIntegerField(blank=True, null=True)
    ds_outros_meio_comunicacao = models.CharField(max_length=50, blank=True, null=True)
    cd_grupo_comunitario = models.SmallIntegerField(blank=True, null=True)
    ds_outros_grupo_comunitario = models.CharField(max_length=50, blank=True, null=True)
    cd_meio_transporte = models.SmallIntegerField(blank=True, null=True)
    ds_outros_meio_transporte = models.CharField(max_length=50, blank=True, null=True)
    observacao = models.CharField(max_length=1024, blank=True, null=True)
    version = models.BigIntegerField()
    cd_usuario = models.ForeignKey('profissionais.Usuarios', models.DO_NOTHING, db_column='cd_usuario')
    dt_usuario = models.DateTimeField()
    dt_cadastro = models.DateTimeField()
    condicao_domicilio = models.SmallIntegerField(blank=True, null=True)
    flag_bolsa_familia = models.CharField(max_length=1, blank=True, null=True)
    flag_cad_unico = models.CharField(max_length=1, blank=True, null=True)
    nis_responsavel = models.CharField(max_length=20, blank=True, null=True)
    cd_eqp_micro_area = models.ForeignKey('EquipeMicroArea', models.DO_NOTHING, db_column='cd_eqp_micro_area', blank=True, null=True)
    version_all = models.BigIntegerField(unique=True)
    cd_usu_cadsus_nis = models.ForeignKey('pacientes.UsuarioCadsus', models.DO_NOTHING, db_column='cd_usu_cadsus_nis', blank=True, null=True)
    uuid_tablet = models.CharField(blank=True, null=True)
    score_estratificacao = models.BigIntegerField(blank=True, null=True)
    flag_bpc = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'endereco_domicilio'

    def __str__(self):
        return f"Domicílio {self.cd_domicilio} - Área/Micro: {self.nr_area or 'N/A'}/{self.nr_micro_area or 'N/A'}"


class EnderecoUsuarioCadsus(models.Model):
    cd_endereco = models.BigIntegerField(primary_key=True)
    public_id = models.UUIDField(default=uuid6.uuid7, editable=False, unique=True, db_index=True, db_column='uuid_publico')
    cd_tipo_logradouro = models.ForeignKey('TipoLogradouroCadsus', models.DO_NOTHING, db_column='cd_tipo_logradouro', blank=True, null=True)
    nm_logradouro = models.CharField(max_length=50)
    nr_logradouro = models.CharField(max_length=7, blank=True, null=True)
    nm_bairro = models.CharField(max_length=72, blank=True, null=True)
    cep = models.CharField(max_length=10, blank=True, null=True)
    nr_telefone = models.CharField(max_length=15, blank=True, null=True)
    cod_cid = models.ForeignKey(Cidade, models.DO_NOTHING, db_column='cod_cid', blank=True, null=True)
    nr_fax = models.CharField(max_length=15, blank=True, null=True)
    ds_uso_municipal = models.CharField(max_length=200, blank=True, null=True)
    st_excluido = models.SmallIntegerField()
    st_ativo = models.SmallIntegerField()
    cd_endereco_interno = models.CharField(max_length=50, blank=True, null=True)
    nm_comp_logradouro = models.CharField(max_length=50, blank=True, null=True)
    dt_alteracao = models.DateTimeField(blank=True, null=True)
    version = models.BigIntegerField()
    ponto_referencia = models.CharField(max_length=100, blank=True, null=True)
    empresa = models.ForeignKey('institucional.Empresa', models.DO_NOTHING, db_column='empresa', blank=True, null=True)
    version_all = models.BigIntegerField(unique=True)
    nr_telefone_referencia = models.CharField(max_length=15, blank=True, null=True)
    keyword = models.CharField(blank=True, null=True)
    uuid_tablet = models.CharField(blank=True, null=True)
    cd_endereco_estruturado = models.ForeignKey('EnderecoEstruturado', models.DO_NOTHING, db_column='cd_endereco_estruturado', blank=True, null=True)
    quadra = models.CharField(max_length=5, blank=True, null=True)
    lote = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'endereco_usuario_cadsus'

    def __str__(self):
        return f"{self.nm_logradouro}, {self.nr_logradouro or 'S/N'} - {self.nm_bairro or ''}"


class TipoLogradouroCnes(models.Model):
    cd_tipo_logradouro = models.CharField(primary_key=True, max_length=3)
    public_id = models.UUIDField(default=uuid6.uuid7, editable=False, unique=True, db_index=True, db_column='uuid_publico')
    ds_tipo_logradouro = models.CharField(max_length=60, blank=True, null=True)
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'tipo_logradouro_cnes'
        db_table_comment = 'CNES - NFCES037'

    def __str__(self):
        return self.ds_tipo_logradouro or self.cd_tipo_logradouro


# =====================================================================
# STUBS TEMPORÁRIOS PARA ESTE APP
# =====================================================================
class Estado(models.Model):
    class Meta: 
        managed = False
        db_table = 'estado'


class EquipeMicroArea(models.Model):
    class Meta: 
        managed = False
        db_table = 'equipe_micro_area'


class TipoLogradouroCadsus(models.Model):
    class Meta: 
        managed = False
        db_table = 'tipo_logradouro_cadsus'


class EnderecoEstruturado(models.Model):
    class Meta: 
        managed = False
        db_table = 'endereco_estruturado'