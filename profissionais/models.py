from django.db import models


class OrgaoEmissor(models.Model):
    cd_orgao_emissor = models.SmallIntegerField(primary_key=True, db_column='cd_orgao_emissor')
    ds_orgao_emissor = models.CharField(max_length=60, db_column='ds_orgao_emissor', blank=True, null=True)
    sg_orgao_emissor = models.CharField(max_length=10, db_column='sg_orgao_emissor', blank=True, null=True)
    fl_saude = models.CharField(max_length=1, db_column='fl_saude', blank=True, null=True)
    cod_conselho_tiss = models.IntegerField(db_column='cod_conselho_tiss', blank=True, null=True)
    oid = models.CharField(max_length=50, db_column='oid', blank=True, null=True)
    version = models.BigIntegerField()
    version_all = models.BigIntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'orgao_emissor'

    def __str__(self):
        if self.sg_orgao_emissor and self.ds_orgao_emissor:
            return f"{self.sg_orgao_emissor} - {self.ds_orgao_emissor}"
        return self.sg_orgao_emissor if self.sg_orgao_emissor else f"Órgão {self.pk}"
    

class TabelaSubgrupoCbo(models.Model):
    class Meta:
        managed = False
        db_table = 'tabela_subgrupo_cbo'

    def __str__(self):
        return f"Subgrupo CBO {self.pk}"


class TabelaCboGrupoAtendimento(models.Model):
    cd_cbo_grupo_atend = models.BigIntegerField(
        db_column='cd_cbo_grupo_atend', 
        primary_key=True
    )
    descricao = models.CharField(
        db_column='descricao', 
        max_length=100,      # Descoberta cirúrgica: limite exato do banco
        blank=False,         # Obrigatoriedade espelhada do is_nullable: NO
        null=False           # Obrigatoriedade espelhada do is_nullable: NO
    )
    version = models.BigIntegerField(
        db_column='version', 
        blank=False,         # Obrigatoriedade espelhada do is_nullable: NO
        null=False           # Obrigatoriedade espelhada do is_nullable: NO
    )
    flag_medico = models.SmallIntegerField(
        db_column='flag_medico', 
        blank=True,          # Permitido pelo banco (is_nullable: YES)
        null=True            # Permitido pelo banco (is_nullable: YES)
    )

    class Meta:
        managed = False  # O banco Neon dita as regras estruturais
        db_table = 'tabela_cbo_grupo_atendimento'
        verbose_name = 'CBO Grupo de Atendimento'
        verbose_name_plural = 'CBO Grupos de Atendimento'

    def __str__(self):
        return f"{self.cd_cbo_grupo_atend} - {self.descricao}"
    

class ProgramaWeb(models.Model):
    cd_prg_web = models.IntegerField(primary_key=True, db_column='cd_prg_web')
    ds_prg_web = models.CharField(max_length=255, db_column='ds_prg_web') 
    cd_prg_pag_principal = models.IntegerField(db_column='cd_prg_pag_principal')
    ativo = models.CharField(max_length=1, db_column='ativo')
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'programa_web'

    def __str__(self):
        return self.ds_prg_web if self.ds_prg_web else f"Programa Web {self.pk}"


class Profissional(models.Model):
    cd_profissional = models.IntegerField(primary_key=True, db_column='cd_profissional')
    nm_profissional = models.CharField(max_length=60, db_column='nm_profissional')
    cpf = models.CharField(max_length=14, blank=True, null=True)
    rua = models.CharField(max_length=60, blank=True, null=True)
    complemento = models.CharField(max_length=60, blank=True, null=True)
    bairro = models.CharField(max_length=60, blank=True, null=True)
    cod_cid = models.ForeignKey('geografia.Cidade', models.DO_NOTHING, db_column='cod_cid', blank=True, null=True)
    numero_rua = models.CharField(max_length=10, blank=True, null=True)
    nm_mae = models.CharField(max_length=60, blank=True, null=True)
    nm_pai = models.CharField(max_length=60, blank=True, null=True)
    dt_nascimento = models.DateField(blank=True, null=True)
    sexo = models.CharField(max_length=1, blank=True, null=True)
    tp_sus_nao_sus = models.CharField(max_length=1, blank=True, null=True)
    cd_tipo_logradouro = models.ForeignKey('geografia.TipoLogradouroCnes', models.DO_NOTHING, db_column='cd_tipo_logradouro', blank=True, null=True)
    cep = models.CharField(max_length=8, blank=True, null=True)
    cd_orgao_emissor = models.SmallIntegerField(db_column='cd_orgao_emissor', blank=True, null=True)
    cd_con_classe = models.SmallIntegerField(db_column='cd_con_classe', blank=True, null=True)
    nr_rg = models.CharField(max_length=15, blank=True, null=True)
    dt_emissao_rg = models.DateField(blank=True, null=True)
    uf_rg = models.CharField(max_length=2, blank=True, null=True)
    cd_cns = models.CharField(max_length=60, blank=True, null=True)
    telefone = models.CharField(max_length=40, blank=True, null=True)
    cod_cid_nasc = models.ForeignKey('geografia.Cidade', models.DO_NOTHING, db_column='cod_cid_nasc', related_name='profissional_cod_cid_nasc_set', blank=True, null=True)
    dt_atualizacao = models.DateTimeField(blank=True, null=True)
    profissional_id_cnes = models.CharField(max_length=16, blank=True, null=True)
    ativo = models.CharField(max_length=1, blank=True, null=True)
    dt_inativacao = models.DateTimeField(blank=True, null=True)
    nr_registro = models.CharField(max_length=50, blank=True, null=True)
    dt_registro = models.DateField(blank=True, null=True)
    regiao_registro = models.CharField(max_length=50, blank=True, null=True)
    cd_usuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='cd_usuario', blank=True, null=True, related_name='profissional_usuario_set')
    tipo = models.CharField(max_length=1, blank=True, null=True)
    erro_importacao = models.TextField(blank=True, null=True)
    referencia = models.CharField(unique=True, max_length=10, blank=True, null=True)
    observacao = models.CharField(max_length=250, blank=True, null=True)
    flag_nao_possui_cns = models.SmallIntegerField(blank=True, null=True)
    version_all = models.BigIntegerField(unique=True)
    cd_tipo_prestador_ipe = models.ForeignKey('institucional.TipoPrestadorIpe', models.DO_NOTHING, db_column='cd_tipo_prestador_ipe', blank=True, null=True)
    uf_conselho_reg = models.CharField(max_length=2, blank=True, null=True)
    chave_biometria = models.TextField(blank=True, null=True)
    cd_cnes_processo = models.ForeignKey('institucional.CnesProcesso', models.DO_NOTHING, db_column='cd_cnes_processo', blank=True, null=True)
    flag_fiscal_visa = models.SmallIntegerField(blank=True, null=True)
    flag_fiscal_capacitado = models.SmallIntegerField(blank=True, null=True)
    escolaridade = models.SmallIntegerField(blank=True, null=True)
    estado_civil = models.SmallIntegerField(blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    vinculo = models.SmallIntegerField(blank=True, null=True)
    cargo = models.CharField(blank=True, null=True)
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'profissional'
        
    def __str__(self):
        return f"{self.nm_profissional} (Registro: {self.nr_registro or 'S/N'})"


class TabelaCbo(models.Model):
    cd_cbo = models.CharField(primary_key=True, max_length=10, db_column='cd_cbo')
    ds_cbo = models.CharField(max_length=150, db_column='ds_cbo')
    cd_grupo_cbo = models.ForeignKey('TabelaSubgrupoCbo', models.DO_NOTHING, db_column='cd_grupo_cbo', blank=True, null=True)
    cd_subgrupo_cbo = models.SmallIntegerField(blank=True, null=True)
    cd_cbo_grupo_atend = models.ForeignKey('TabelaCboGrupoAtendimento', models.DO_NOTHING, db_column='cd_cbo_grupo_atend', blank=True, null=True)
    nivel_ensino = models.SmallIntegerField(blank=True, null=True)
    ativo = models.SmallIntegerField()
    tipo_profissional_saude = models.SmallIntegerField(blank=True, null=True)
    version = models.BigIntegerField()
    version_all = models.BigIntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'tabela_cbo'

    def __str__(self):
        return f"{self.cd_cbo} - {self.ds_cbo}"


class Usuarios(models.Model):
    cd_usuario = models.DecimalField(primary_key=True, max_digits=6, decimal_places=0, db_column='cd_usuario')
    cd_modulo = models.ForeignKey('institucional.Modulo', models.DO_NOTHING, db_column='cd_modulo', blank=True, null=True)
    ds_login = models.CharField(unique=True, max_length=100, db_column='ds_login')
    nm_usuario = models.CharField(max_length=50, db_column='nm_usuario')
    dt_criacao = models.DateField()
    ds_status = models.CharField(max_length=1)
    senha = models.CharField()
    ds_nivel = models.CharField(max_length=1)
    navegador_padrao = models.CharField(max_length=200, blank=True, null=True)
    dir_temp = models.CharField(max_length=50, blank=True, null=True)
    empresa_padrao = models.ForeignKey('institucional.Empresa', models.DO_NOTHING, db_column='empresa_padrao', blank=True, null=True)
    ds_email = models.CharField(max_length=100, blank=True, null=True)
    cd_profissional = models.ForeignKey('Profissional', models.DO_NOTHING, db_column='cd_profissional', blank=True, null=True, related_name='usuario_profissional_set')
    exibe_nome_atalho = models.CharField(max_length=1, blank=True, null=True)
    cod_centro_custo = models.ForeignKey('institucional.CentroCusto', models.DO_NOTHING, db_column='cod_centro_custo', blank=True, null=True)
    tempo_sessao = models.IntegerField(blank=True, null=True)
    dt_ult_acesso = models.DateTimeField(blank=True, null=True)
    qt_acesso = models.SmallIntegerField(blank=True, null=True)
    identificador = models.CharField(unique=True, blank=True, null=True)
    flag_identificavel = models.CharField(max_length=1, blank=True, null=True)
    cd_usuario_cad = models.ForeignKey('self', models.DO_NOTHING, db_column='cd_usuario_cad')
    flag_usu_temporario = models.SmallIntegerField()
    data_registro = models.DateTimeField(blank=True, null=True)
    dias_expirar_senha = models.SmallIntegerField(blank=True, null=True)
    tp_usuario = models.SmallIntegerField()
    flag_receber_email_msg_interna = models.CharField(max_length=1, blank=True, null=True)
    cpf = models.CharField(max_length=11, blank=True, null=True)
    id_integracao = models.CharField(blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    cd_certificado_digital = models.ForeignKey('faturamento.GerenciadorArquivo', models.DO_NOTHING, db_column='cd_certificado_digital', blank=True, null=True)
    cd_prg_web = models.ForeignKey('ProgramaWeb', models.DO_NOTHING, db_column='cd_prg_web', blank=True, null=True)
    ds_cargo = models.CharField(max_length=50, blank=True, null=True)
    flag_termo_uso = models.SmallIntegerField(blank=True, null=True)
    dt_ult_tent_acesso = models.DateTimeField(blank=True, null=True)
    public_key_certificate = models.CharField(unique=True, blank=True, null=True)
    dt_inicial_ferias = models.DateTimeField(blank=True, null=True)
    dt_final_ferias = models.DateTimeField(blank=True, null=True)
    dt_termo_uso = models.DateTimeField(blank=True, null=True)
    flag_termo_uso_mobile = models.SmallIntegerField(blank=True, null=True)
    dt_termo_uso_mobile = models.DateTimeField(blank=True, null=True)
    funcionario_celk = models.SmallIntegerField(blank=True, null=True)
    flag_habilita_app_fru = models.CharField(max_length=3, blank=True, null=True)
    data_termo_fru = models.DateTimeField(blank=True, null=True)
    tp_certificado = models.IntegerField(blank=True, null=True)
    provedor_certificado = models.IntegerField(blank=True, null=True)
    version = models.BigIntegerField()
    version_all = models.BigIntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'usuarios'

    def __str__(self):
        return f"{self.ds_login} - {self.nm_usuario}"