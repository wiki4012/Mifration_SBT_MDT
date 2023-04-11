# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AplInfaWorkflowsInfo(models.Model):
    repo_name = models.CharField(max_length=20, blank=True, null=True)
    is_service = models.CharField(max_length=20, blank=True, null=True)
    folder_name = models.CharField(max_length=30, blank=True, null=True)
    workflow_name = models.CharField(max_length=100, blank=True, null=True)
    workflow_desc = models.CharField(max_length=100, blank=True, null=True)
    business = models.CharField(max_length=20, blank=True, null=True)
    application_name = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    logdate = models.DateField(blank=True, null=True)
    order_no = models.IntegerField(blank=True, null=True)
    id = models.CharField(max_length=32, blank=True, null=True)
    script_path = models.CharField(max_length=200, blank=True, null=True)
    script_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apl_infa_workflows_info'


class AplPlmEmployee(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    version = models.IntegerField()
    create_ts = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    update_ts = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    delete_ts = models.DateTimeField(blank=True, null=True)
    deleted_by = models.CharField(max_length=50, blank=True, null=True)
    user = models.ForeignKey('SecUser', models.DO_NOTHING, blank=True, null=True)
    position_field = models.CharField(db_column='position_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'apl_plm_employee'
# Unable to inspect table 'apl_plm_employee_sitemaster_link'
# The error was: ORA-00942: table or view does not exist


class AplPlmSitemaster(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    version = models.IntegerField()
    create_ts = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    update_ts = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    delete_ts = models.DateTimeField(blank=True, null=True)
    deleted_by = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.ForeignKey('SecGroup', models.DO_NOTHING, blank=True, null=True)
    siteid = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apl_plm_sitemaster'


class DbchsHelpContext(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    version = models.IntegerField()
    create_ts = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    update_ts = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    delete_ts = models.DateTimeField(blank=True, null=True)
    deleted_by = models.CharField(max_length=50, blank=True, null=True)
    screen_id = models.CharField(max_length=255, blank=True, null=True)
    component_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dbchs_help_context'


class DbchsHelptext(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    version = models.IntegerField()
    create_ts = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    update_ts = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    delete_ts = models.DateTimeField(blank=True, null=True)
    deleted_by = models.CharField(max_length=50, blank=True, null=True)
    text = models.TextField()
    help_context = models.ForeignKey(DbchsHelpContext, models.DO_NOTHING, blank=True, null=True)
    category = models.ForeignKey('DbchsHelptextCategory', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'dbchs_helptext'


class DbchsHelptextCategory(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    version = models.IntegerField()
    create_ts = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    update_ts = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    delete_ts = models.DateTimeField(blank=True, null=True)
    deleted_by = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    context_independent = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'dbchs_helptext_category'


class Demo3Returnmessages(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    version = models.IntegerField()
    create_ts = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    update_ts = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    delete_ts = models.DateTimeField(blank=True, null=True)
    deleted_by = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'demo3_returnmessages'


class ReportGroup(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    create_ts = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    version = models.BigIntegerField(blank=True, null=True)
    update_ts = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    delete_ts = models.DateTimeField(blank=True, null=True)
    deleted_by = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=255)
    code = models.CharField(max_length=255, blank=True, null=True)
    locale_names = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_group'


class ReportReport(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    create_ts = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    version = models.BigIntegerField(blank=True, null=True)
    update_ts = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    delete_ts = models.DateTimeField(blank=True, null=True)
    deleted_by = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    locale_names = models.TextField(blank=True, null=True)
    group = models.ForeignKey(ReportGroup, models.DO_NOTHING)
    default_template = models.ForeignKey('ReportTemplate', models.DO_NOTHING, blank=True, null=True)
    xml = models.TextField(blank=True, null=True)
    roles_idx = models.CharField(max_length=1000, blank=True, null=True)
    screens_idx = models.CharField(max_length=1000, blank=True, null=True)
    input_entity_types_idx = models.CharField(max_length=1000, blank=True, null=True)
    rest_access = models.CharField(max_length=1, blank=True, null=True)
    is_system = models.CharField(max_length=1, blank=True, null=True)
    report_type = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_report'


class ReportTemplate(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    create_ts = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    version = models.BigIntegerField(blank=True, null=True)
    update_ts = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    delete_ts = models.DateTimeField(blank=True, null=True)
    deleted_by = models.CharField(max_length=50, blank=True, null=True)
    report = models.ForeignKey(ReportReport, models.DO_NOTHING)
    code = models.CharField(max_length=50, blank=True, null=True)
    output_type = models.BigIntegerField()
    is_default = models.CharField(max_length=1, blank=True, null=True)
    is_custom = models.CharField(max_length=1, blank=True, null=True)
    is_alterable_output = models.CharField(max_length=1, blank=True, null=True)
    custom_defined_by = models.BigIntegerField(blank=True, null=True)
    custom_class = models.CharField(max_length=4000, blank=True, null=True)
    output_name_pattern = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=500, blank=True, null=True)
    content = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_template'


class SecConstraint(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    create_ts = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    version = models.BigIntegerField(blank=True, null=True)
    update_ts = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    delete_ts = models.DateTimeField(blank=True, null=True)
    deleted_by = models.CharField(max_length=50, blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    check_type = models.CharField(max_length=50, blank=True, null=True)
    operation_type = models.CharField(max_length=50, blank=True, null=True)
    entity_name = models.CharField(max_length=255)
    join_clause = models.CharField(max_length=500, blank=True, null=True)
    where_clause = models.CharField(max_length=1000, blank=True, null=True)
    groovy_script = models.TextField(blank=True, null=True)
    filter_xml = models.TextField(blank=True, null=True)
    is_active = models.CharField(max_length=1, blank=True, null=True)
    group = models.ForeignKey('SecGroup', models.DO_NOTHING, blank=True, null=True)
    sys_tenant_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sec_constraint'


class SecEntityLog(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    create_ts = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    event_ts = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('SecUser', models.DO_NOTHING, blank=True, null=True)
    change_type = models.CharField(max_length=1, blank=True, null=True)
    entity = models.CharField(max_length=100, blank=True, null=True)
    entity_id = models.CharField(max_length=32, blank=True, null=True)
    string_entity_id = models.CharField(max_length=255, blank=True, null=True)
    int_entity_id = models.BigIntegerField(blank=True, null=True)
    long_entity_id = models.FloatField(blank=True, null=True)
    changes = models.TextField(blank=True, null=True)
    entity_instance_name = models.CharField(max_length=1000, blank=True, null=True)
    sys_tenant_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sec_entity_log'


class SecFilter(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    create_ts = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    version = models.BigIntegerField(blank=True, null=True)
    update_ts = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    delete_ts = models.DateTimeField(blank=True, null=True)
    deleted_by = models.CharField(max_length=50, blank=True, null=True)
    component = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=200, blank=True, null=True)
    xml = models.TextField(blank=True, null=True)
    user = models.ForeignKey('SecUser', models.DO_NOTHING, blank=True, null=True)
    global_default = models.CharField(max_length=1, blank=True, null=True)
    sys_tenant_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sec_filter'


class SecGroup(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    create_ts = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    version = models.BigIntegerField(blank=True, null=True)
    update_ts = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    delete_ts = models.DateTimeField(blank=True, null=True)
    deleted_by = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    sys_tenant_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sec_group'


class SecGroupHierarchy(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    create_ts = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    group = models.ForeignKey(SecGroup, models.DO_NOTHING, blank=True, null=True)
    parent = models.ForeignKey(SecGroup, models.DO_NOTHING, blank=True, null=True)
    hierarchy_level = models.BigIntegerField(blank=True, null=True)
    sys_tenant_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sec_group_hierarchy'


class SecLocalizedConstraintMsg(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    create_ts = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    version = models.BigIntegerField(blank=True, null=True)
    update_ts = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    delete_ts = models.DateTimeField(blank=True, null=True)
    deleted_by = models.CharField(max_length=50, blank=True, null=True)
    entity_name = models.CharField(max_length=255)
    operation_type = models.CharField(max_length=50)
    values_field = models.TextField(db_column='values_', blank=True, null=True)  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'sec_localized_constraint_msg'


class SecLoggedAttr(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    create_ts = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    entity = models.ForeignKey('SecLoggedEntity', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sec_logged_attr'


class SecLoggedEntity(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    create_ts = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    auto = models.CharField(max_length=1, blank=True, null=True)
    manual = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sec_logged_entity'


class SecPermission(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    create_ts = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    version = models.BigIntegerField(blank=True, null=True)
    update_ts = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    delete_ts = models.DateTimeField(blank=True, null=True)
    deleted_by = models.CharField(max_length=50, blank=True, null=True)
    permission_type = models.BigIntegerField(blank=True, null=True)
    target = models.CharField(max_length=100, blank=True, null=True)
    value_field = models.BigIntegerField(db_column='value_', blank=True, null=True)  # Field renamed because it ended with '_'.
    role = models.ForeignKey('SecRole', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sec_permission'


class SecPresentation(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    create_ts = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    update_ts = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    component = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    xml = models.CharField(max_length=4000, blank=True, null=True)
    user = models.ForeignKey('SecUser', models.DO_NOTHING, blank=True, null=True)
    is_auto_save = models.CharField(max_length=1, blank=True, null=True)
    sys_tenant_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sec_presentation'


class SecRememberMe(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    create_ts = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    version = models.BigIntegerField(blank=True, null=True)
    user = models.ForeignKey('SecUser', models.DO_NOTHING)
    token = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'sec_remember_me'


class SecRole(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    create_ts = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    version = models.BigIntegerField(blank=True, null=True)
    update_ts = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    delete_ts = models.DateTimeField(blank=True, null=True)
    deleted_by = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=255)
    loc_name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    is_default_role = models.CharField(max_length=1, blank=True, null=True)
    role_type = models.BigIntegerField(blank=True, null=True)
    sys_tenant_id = models.CharField(max_length=255, blank=True, null=True)
    security_scope = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sec_role'


class SecScreenHistory(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    create_ts = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    user = models.ForeignKey('SecUser', models.DO_NOTHING, blank=True, null=True)
    caption = models.CharField(max_length=255, blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    entity_id = models.CharField(max_length=32, blank=True, null=True)
    substituted_user = models.ForeignKey('SecUser', models.DO_NOTHING, blank=True, null=True)
    string_entity_id = models.CharField(max_length=255, blank=True, null=True)
    int_entity_id = models.BigIntegerField(blank=True, null=True)
    long_entity_id = models.FloatField(blank=True, null=True)
    sys_tenant_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sec_screen_history'


class SecSearchFolder(models.Model):
    folder = models.OneToOneField('SysFolder', models.DO_NOTHING, primary_key=True)
    filter_component = models.CharField(max_length=200, blank=True, null=True)
    filter_xml = models.TextField(blank=True, null=True)
    user = models.ForeignKey('SecUser', models.DO_NOTHING, blank=True, null=True)
    presentation = models.ForeignKey(SecPresentation, models.DO_NOTHING, blank=True, null=True)
    apply_default = models.CharField(max_length=1, blank=True, null=True)
    is_set = models.CharField(max_length=1, blank=True, null=True)
    entity_type = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sec_search_folder'


class SecSessionAttr(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    create_ts = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    version = models.BigIntegerField(blank=True, null=True)
    update_ts = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    delete_ts = models.DateTimeField(blank=True, null=True)
    deleted_by = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    str_value = models.CharField(max_length=1000, blank=True, null=True)
    datatype = models.CharField(max_length=20, blank=True, null=True)
    group = models.ForeignKey(SecGroup, models.DO_NOTHING, blank=True, null=True)
    sys_tenant_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sec_session_attr'


class SecSessionLog(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    version = models.BigIntegerField()
    create_ts = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    update_ts = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    delete_ts = models.DateTimeField(blank=True, null=True)
    deleted_by = models.CharField(max_length=50, blank=True, null=True)
    session_id = models.CharField(max_length=32)
    user = models.ForeignKey('SecUser', models.DO_NOTHING)
    substituted_user = models.ForeignKey('SecUser', models.DO_NOTHING, blank=True, null=True)
    user_data = models.TextField(blank=True, null=True)
    last_action = models.BigIntegerField()
    client_info = models.CharField(max_length=512, blank=True, null=True)
    client_type = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    started_ts = models.DateTimeField(blank=True, null=True)
    finished_ts = models.DateTimeField(blank=True, null=True)
    server_id = models.CharField(max_length=128, blank=True, null=True)
    sys_tenant_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sec_session_log'


class SecUser(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    create_ts = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    version = models.BigIntegerField(blank=True, null=True)
    update_ts = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    delete_ts = models.DateTimeField(blank=True, null=True)
    deleted_by = models.CharField(max_length=50, blank=True, null=True)
    login = models.CharField(max_length=50)
    login_lc = models.CharField(max_length=50)
    password = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    position_field = models.CharField(db_column='position_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    email = models.CharField(max_length=100, blank=True, null=True)
    language_field = models.CharField(db_column='language_', max_length=20, blank=True, null=True)  # Field renamed because it ended with '_'.
    time_zone = models.CharField(max_length=50, blank=True, null=True)
    time_zone_auto = models.CharField(max_length=1, blank=True, null=True)
    active = models.CharField(max_length=1, blank=True, null=True)
    group = models.ForeignKey(SecGroup, models.DO_NOTHING, blank=True, null=True)
    ip_mask = models.CharField(max_length=200, blank=True, null=True)
    change_password_at_logon = models.CharField(max_length=1, blank=True, null=True)
    password_encryption = models.CharField(max_length=50, blank=True, null=True)
    group_names = models.CharField(max_length=255, blank=True, null=True)
    sys_tenant_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sec_user'


class SecUserRole(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    create_ts = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    version = models.BigIntegerField(blank=True, null=True)
    update_ts = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    delete_ts = models.DateTimeField(blank=True, null=True)
    deleted_by = models.CharField(max_length=50, blank=True, null=True)
    user = models.ForeignKey(SecUser, models.DO_NOTHING, blank=True, null=True)
    role = models.ForeignKey(SecRole, models.DO_NOTHING, blank=True, null=True)
    role_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sec_user_role'


class SecUserSetting(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    create_ts = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    user = models.ForeignKey(SecUser, models.DO_NOTHING, blank=True, null=True)
    client_type = models.CharField(max_length=1, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    value_field = models.TextField(db_column='value_', blank=True, null=True)  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'sec_user_setting'


class SecUserSubstitution(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    create_ts = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    version = models.BigIntegerField(blank=True, null=True)
    update_ts = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    delete_ts = models.DateTimeField(blank=True, null=True)
    deleted_by = models.CharField(max_length=50, blank=True, null=True)
    user = models.ForeignKey(SecUser, models.DO_NOTHING)
    substituted_user = models.ForeignKey(SecUser, models.DO_NOTHING)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    sys_tenant_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sec_user_substitution'


class SysAccessToken(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    create_ts = models.DateTimeField(blank=True, null=True)
    token_value = models.CharField(max_length=255, blank=True, null=True)
    token_bytes = models.BinaryField(blank=True, null=True)
    authentication_key = models.CharField(max_length=255, blank=True, null=True)
    authentication_bytes = models.BinaryField(blank=True, null=True)
    expiry = models.DateTimeField(blank=True, null=True)
    user_login = models.CharField(max_length=50, blank=True, null=True)
    locale = models.CharField(max_length=200, blank=True, null=True)
    refresh_token_value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_access_token'


class SysAppFolder(models.Model):
    folder = models.OneToOneField('SysFolder', models.DO_NOTHING, primary_key=True)
    filter_component = models.CharField(max_length=200, blank=True, null=True)
    filter_xml = models.TextField(blank=True, null=True)
    visibility_script = models.TextField(blank=True, null=True)
    quantity_script = models.TextField(blank=True, null=True)
    apply_default = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_app_folder'


class SysAttrValue(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    create_ts = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    version = models.BigIntegerField(blank=True, null=True)
    update_ts = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    delete_ts = models.DateTimeField(blank=True, null=True)
    deleted_by = models.CharField(max_length=50, blank=True, null=True)
    category_attr = models.ForeignKey('SysCategoryAttr', models.DO_NOTHING)
    entity_id = models.CharField(max_length=32, blank=True, null=True)
    string_entity_id = models.CharField(max_length=255, blank=True, null=True)
    int_entity_id = models.BigIntegerField(blank=True, null=True)
    long_entity_id = models.FloatField(blank=True, null=True)
    string_value = models.CharField(max_length=4000, blank=True, null=True)
    integer_value = models.BigIntegerField(blank=True, null=True)
    double_value = models.DecimalField(max_digits=36, decimal_places=6, blank=True, null=True)
    date_value = models.DateTimeField(blank=True, null=True)
    boolean_value = models.CharField(max_length=1, blank=True, null=True)
    entity_value = models.CharField(max_length=32, blank=True, null=True)
    string_entity_value = models.CharField(max_length=255, blank=True, null=True)
    int_entity_value = models.BigIntegerField(blank=True, null=True)
    long_entity_value = models.FloatField(blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    date_wo_time_value = models.DateField(blank=True, null=True)
    decimal_value = models.DecimalField(max_digits=36, decimal_places=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_attr_value'


class SysCategory(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    create_ts = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    version = models.BigIntegerField(blank=True, null=True)
    update_ts = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    delete_ts = models.DateTimeField(blank=True, null=True)
    deleted_by = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=255)
    special = models.CharField(max_length=50, blank=True, null=True)
    entity_type = models.CharField(max_length=100)
    is_default = models.CharField(max_length=1, blank=True, null=True)
    discriminator = models.BigIntegerField(blank=True, null=True)
    locale_names = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_category'


class SysCategoryAttr(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    create_ts = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    version = models.BigIntegerField(blank=True, null=True)
    update_ts = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    delete_ts = models.DateTimeField(blank=True, null=True)
    deleted_by = models.CharField(max_length=50, blank=True, null=True)
    category_entity_type = models.CharField(max_length=4000, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=255)
    category = models.ForeignKey(SysCategory, models.DO_NOTHING)
    entity_class = models.CharField(max_length=500, blank=True, null=True)
    data_type = models.CharField(max_length=200, blank=True, null=True)
    default_string = models.CharField(max_length=4000, blank=True, null=True)
    default_int = models.BigIntegerField(blank=True, null=True)
    default_double = models.DecimalField(max_digits=36, decimal_places=6, blank=True, null=True)
    default_date = models.DateTimeField(blank=True, null=True)
    default_date_is_current = models.CharField(max_length=1, blank=True, null=True)
    default_boolean = models.CharField(max_length=1, blank=True, null=True)
    default_entity_value = models.CharField(max_length=32, blank=True, null=True)
    default_str_entity_value = models.CharField(max_length=255, blank=True, null=True)
    default_int_entity_value = models.BigIntegerField(blank=True, null=True)
    default_long_entity_value = models.FloatField(blank=True, null=True)
    enumeration = models.CharField(max_length=500, blank=True, null=True)
    order_no = models.BigIntegerField(blank=True, null=True)
    screen = models.CharField(max_length=255, blank=True, null=True)
    required = models.CharField(max_length=1, blank=True, null=True)
    lookup = models.CharField(max_length=1, blank=True, null=True)
    target_screens = models.CharField(max_length=4000, blank=True, null=True)
    width = models.CharField(max_length=20, blank=True, null=True)
    rows_count = models.BigIntegerField(blank=True, null=True)
    is_collection = models.CharField(max_length=1, blank=True, null=True)
    join_clause = models.CharField(max_length=4000, blank=True, null=True)
    where_clause = models.CharField(max_length=4000, blank=True, null=True)
    filter_xml = models.TextField(blank=True, null=True)
    locale_names = models.CharField(max_length=1000, blank=True, null=True)
    enumeration_locales = models.TextField(blank=True, null=True)
    default_date_wo_time = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    locale_descriptions = models.CharField(max_length=4000, blank=True, null=True)
    default_decimal = models.DecimalField(max_digits=36, decimal_places=10, blank=True, null=True)
    attribute_configuration_json = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_category_attr'


class SysConfig(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    create_ts = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    version = models.BigIntegerField(blank=True, null=True)
    update_ts = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=255)
    value_field = models.TextField(db_column='value_')  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'sys_config'


class SysDbChangelog(models.Model):
    script_name = models.CharField(primary_key=True, max_length=300)
    create_ts = models.DateTimeField(blank=True, null=True)
    is_init = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_db_changelog'


class SysEntitySnapshot(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    create_ts = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    entity_meta_class = models.CharField(max_length=50)
    entity_id = models.CharField(max_length=32, blank=True, null=True)
    string_entity_id = models.CharField(max_length=255, blank=True, null=True)
    int_entity_id = models.BigIntegerField(blank=True, null=True)
    long_entity_id = models.FloatField(blank=True, null=True)
    author = models.ForeignKey(SecUser, models.DO_NOTHING)
    view_xml = models.TextField()
    snapshot_xml = models.TextField()
    snapshot_date = models.DateTimeField()
    sys_tenant_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_entity_snapshot'


class SysEntityStatistics(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    create_ts = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    update_ts = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    instance_count = models.FloatField(blank=True, null=True)
    fetch_ui = models.BigIntegerField(blank=True, null=True)
    max_fetch_ui = models.BigIntegerField(blank=True, null=True)
    lazy_collection_threshold = models.BigIntegerField(blank=True, null=True)
    lookup_screen_threshold = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_entity_statistics'


class SysFile(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    create_ts = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    version = models.BigIntegerField(blank=True, null=True)
    update_ts = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    delete_ts = models.DateTimeField(blank=True, null=True)
    deleted_by = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=500)
    ext = models.CharField(max_length=20, blank=True, null=True)
    file_size = models.BigIntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    sys_tenant_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_file'


class SysFolder(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    create_ts = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    version = models.BigIntegerField(blank=True, null=True)
    update_ts = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    delete_ts = models.DateTimeField(blank=True, null=True)
    deleted_by = models.CharField(max_length=50, blank=True, null=True)
    folder_type = models.CharField(max_length=1, blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    tab_name = models.CharField(max_length=100, blank=True, null=True)
    sort_order = models.BigIntegerField(blank=True, null=True)
    sys_tenant_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_folder'


class SysFtsQueue(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    create_ts = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    entity_id = models.CharField(max_length=32, blank=True, null=True)
    string_entity_id = models.CharField(max_length=255, blank=True, null=True)
    int_entity_id = models.BigIntegerField(blank=True, null=True)
    long_entity_id = models.FloatField(blank=True, null=True)
    entity_name = models.CharField(max_length=200, blank=True, null=True)
    change_type = models.CharField(max_length=1, blank=True, null=True)
    source_host = models.CharField(max_length=255, blank=True, null=True)
    indexing_host = models.CharField(max_length=255, blank=True, null=True)
    fake = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_fts_queue'


class SysJmxInstance(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    create_ts = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    version = models.BigIntegerField(blank=True, null=True)
    update_ts = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    delete_ts = models.DateTimeField(blank=True, null=True)
    deleted_by = models.CharField(max_length=50, blank=True, null=True)
    node_name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=500)
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'sys_jmx_instance'


class SysLockConfig(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    create_ts = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    timeout_sec = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_lock_config'


class SysQueryResult(models.Model):
    id = models.FloatField(primary_key=True)
    session_id = models.CharField(max_length=32)
    query_key = models.BigIntegerField()
    entity_id = models.CharField(max_length=32, blank=True, null=True)
    string_entity_id = models.CharField(max_length=255, blank=True, null=True)
    int_entity_id = models.BigIntegerField(blank=True, null=True)
    long_entity_id = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_query_result'


class SysRefreshToken(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    create_ts = models.DateTimeField(blank=True, null=True)
    token_value = models.CharField(max_length=255, blank=True, null=True)
    token_bytes = models.BinaryField(blank=True, null=True)
    authentication_bytes = models.BinaryField(blank=True, null=True)
    expiry = models.DateTimeField(blank=True, null=True)
    user_login = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_refresh_token'


class SysScheduledExecution(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    create_ts = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    task = models.ForeignKey('SysScheduledTask', models.DO_NOTHING, blank=True, null=True)
    server = models.CharField(max_length=512, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    finish_time = models.DateTimeField(blank=True, null=True)
    result = models.TextField(blank=True, null=True)
    sys_tenant_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_scheduled_execution'


class SysScheduledTask(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    create_ts = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    update_ts = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    delete_ts = models.DateTimeField(blank=True, null=True)
    deleted_by = models.CharField(max_length=50, blank=True, null=True)
    defined_by = models.CharField(max_length=1, blank=True, null=True)
    class_name = models.CharField(max_length=500, blank=True, null=True)
    script_name = models.CharField(max_length=500, blank=True, null=True)
    bean_name = models.CharField(max_length=50, blank=True, null=True)
    method_name = models.CharField(max_length=50, blank=True, null=True)
    method_params = models.CharField(max_length=4000, blank=True, null=True)
    user_name = models.CharField(max_length=50, blank=True, null=True)
    is_singleton = models.CharField(max_length=1, blank=True, null=True)
    is_active = models.CharField(max_length=1, blank=True, null=True)
    period = models.BigIntegerField(blank=True, null=True)
    timeout = models.BigIntegerField(blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    time_frame = models.BigIntegerField(blank=True, null=True)
    start_delay = models.BigIntegerField(blank=True, null=True)
    permitted_servers = models.CharField(max_length=4000, blank=True, null=True)
    log_start = models.CharField(max_length=1, blank=True, null=True)
    log_finish = models.CharField(max_length=1, blank=True, null=True)
    last_start_time = models.DateTimeField(blank=True, null=True)
    last_start_server = models.CharField(max_length=512, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    cron = models.CharField(max_length=100, blank=True, null=True)
    scheduling_type = models.CharField(max_length=1, blank=True, null=True)
    period_field = models.BigIntegerField(db_column='period_', blank=True, null=True)  # Field renamed because it ended with '_'.
    sys_tenant_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_scheduled_task'


class SysSendingAttachment(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    create_ts = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    version = models.BigIntegerField(blank=True, null=True)
    update_ts = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    delete_ts = models.DateTimeField(blank=True, null=True)
    deleted_by = models.CharField(max_length=50, blank=True, null=True)
    message = models.ForeignKey('SysSendingMessage', models.DO_NOTHING, blank=True, null=True)
    content = models.BinaryField(blank=True, null=True)
    content_id = models.CharField(max_length=50, blank=True, null=True)
    content_file = models.ForeignKey(SysFile, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=500, blank=True, null=True)
    disposition = models.CharField(max_length=50, blank=True, null=True)
    text_encoding = models.CharField(max_length=50, blank=True, null=True)
    sys_tenant_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_sending_attachment'


class SysSendingMessage(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    create_ts = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    version = models.BigIntegerField(blank=True, null=True)
    update_ts = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    delete_ts = models.DateTimeField(blank=True, null=True)
    deleted_by = models.CharField(max_length=50, blank=True, null=True)
    address_to = models.TextField(blank=True, null=True)
    address_from = models.CharField(max_length=100, blank=True, null=True)
    caption = models.CharField(max_length=500, blank=True, null=True)
    email_headers = models.CharField(max_length=500, blank=True, null=True)
    content_text = models.TextField(blank=True, null=True)
    content_text_file = models.ForeignKey(SysFile, models.DO_NOTHING, blank=True, null=True)
    deadline = models.DateTimeField(blank=True, null=True)
    status = models.BigIntegerField(blank=True, null=True)
    date_sent = models.DateTimeField(blank=True, null=True)
    attempts_count = models.BigIntegerField(blank=True, null=True)
    attempts_made = models.BigIntegerField(blank=True, null=True)
    attachments_name = models.TextField(blank=True, null=True)
    body_content_type = models.CharField(max_length=50, blank=True, null=True)
    address_cc = models.TextField(blank=True, null=True)
    address_bcc = models.TextField(blank=True, null=True)
    sys_tenant_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_sending_message'


class SysServer(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    create_ts = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    update_ts = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    is_running = models.CharField(max_length=1, blank=True, null=True)
    data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_server'


class ZkpiManualDate(models.Model):
    mannual_kpi_id = models.BigAutoField(primary_key=True)
    team_name = models.CharField(max_length=500, blank=True, null=True)
    kpi_date = models.DateTimeField(blank=True, null=True)
    shift = models.CharField(max_length=10, blank=True, null=True)
    graph_id = models.CharField(max_length=500, blank=True, null=True)
    kpi_name = models.CharField(max_length=500, blank=True, null=True)
    kpi_value = models.FloatField(blank=True, null=True)
    kpi_type = models.CharField(max_length=500, blank=True, null=True)
    monthly_value = models.FloatField(blank=True, null=True)
    weighted_avg = models.BigIntegerField(blank=True, null=True)
    comments = models.CharField(max_length=1000, blank=True, null=True)
    flag = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zkpi_manual_date'


class ZsbtAttendance(models.Model):
    att_id = models.BigAutoField(primary_key=True)
    attendance = models.CharField(max_length=20, blank=True, null=True)
    att_date = models.DateTimeField(blank=True, null=True)
    shift = models.CharField(max_length=20, blank=True, null=True)
    team_member = models.CharField(max_length=400, blank=True, null=True)
    team_name = models.CharField(max_length=400, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zsbt_attendance'


class ZsbtBannerDetails(models.Model):
    ban_id = models.BigAutoField(primary_key=True)
    lastupdateddatetime = models.DateTimeField(blank=True, null=True)
    team_name = models.CharField(max_length=400, blank=True, null=True)
    banner_details = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zsbt_banner_details'


class ZsbtCaPa(models.Model):
    ca_paid = models.BigAutoField(primary_key=True)
    kpi = models.CharField(max_length=600, blank=True, null=True)
    team_name = models.CharField(max_length=600, blank=True, null=True)
    kpihiton = models.DateTimeField(blank=True, null=True)
    capa = models.CharField(max_length=2000, blank=True, null=True)
    what = models.CharField(max_length=2000, blank=True, null=True)
    who = models.CharField(max_length=2000, blank=True, null=True)
    when_field = models.CharField(db_column='when_', max_length=2000, blank=True, null=True)  # Field renamed because it ended with '_'.
    status = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zsbt_ca_pa'


class ZsbtCapa5Why(models.Model):
    why_id = models.BigAutoField(primary_key=True)
    kpi = models.CharField(max_length=400, blank=True, null=True)
    team_name = models.CharField(max_length=400, blank=True, null=True)
    kpihiton = models.DateTimeField(blank=True, null=True)
    main_cause = models.CharField(max_length=600, blank=True, null=True)
    sub_cause1 = models.CharField(max_length=600, blank=True, null=True)
    sub_cause2 = models.CharField(max_length=600, blank=True, null=True)
    sub_cause3 = models.CharField(max_length=600, blank=True, null=True)
    root_cause = models.CharField(max_length=600, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zsbt_capa_5why'


class ZsbtCapaActionable(models.Model):
    act_id = models.BigAutoField(primary_key=True)
    kpi = models.CharField(max_length=400, blank=True, null=True)
    team_name = models.CharField(max_length=400, blank=True, null=True)
    creation_date = models.DateTimeField(blank=True, null=True)
    closure_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=256, blank=True, null=True)
    team_member = models.CharField(max_length=400, blank=True, null=True)
    comments = models.CharField(max_length=600, blank=True, null=True)
    last_updatedon = models.DateTimeField(blank=True, null=True)
    what = models.CharField(max_length=600, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zsbt_capa_actionable'


class ZsbtCapaRecordsMaster(models.Model):
    capaid = models.BigAutoField(primary_key=True)
    kpi = models.CharField(max_length=400, blank=True, null=True)
    team_name = models.CharField(max_length=400, blank=True, null=True)
    kpihiton = models.DateTimeField(blank=True, null=True)
    date_allocation = models.DateTimeField(blank=True, null=True)
    date_submission = models.DateTimeField(blank=True, null=True)
    participants_names = models.CharField(max_length=400, blank=True, null=True)
    what = models.CharField(max_length=800, blank=True, null=True)
    where_s1 = models.CharField(max_length=800, blank=True, null=True)
    when_s1 = models.CharField(max_length=800, blank=True, null=True)
    who = models.CharField(max_length=800, blank=True, null=True)
    why = models.CharField(max_length=800, blank=True, null=True)
    howbig = models.CharField(max_length=800, blank=True, null=True)
    evidance_links = models.TextField(blank=True, null=True)  # This field type is a guess.
    correction = models.CharField(max_length=600, blank=True, null=True)
    analyse_man = models.CharField(max_length=400, blank=True, null=True)
    analyse_method = models.CharField(max_length=400, blank=True, null=True)
    analyse_measurement = models.CharField(max_length=400, blank=True, null=True)
    analyse_machine = models.CharField(max_length=400, blank=True, null=True)
    analyse_material = models.CharField(max_length=400, blank=True, null=True)
    analyse_enviornment = models.CharField(max_length=400, blank=True, null=True)
    brainstorming_tool = models.CharField(max_length=400, blank=True, null=True)
    problem = models.CharField(max_length=400, blank=True, null=True)
    make_it_stick = models.CharField(max_length=400, blank=True, null=True)
    pm_schedule = models.CharField(max_length=400, blank=True, null=True)
    other_s = models.CharField(max_length=2000, blank=True, null=True)
    prepared_by = models.CharField(max_length=800, blank=True, null=True)
    prepared_by_date = models.DateTimeField(blank=True, null=True)
    reviewed_by = models.CharField(max_length=400, blank=True, null=True)
    reviewed_by_date = models.DateTimeField(blank=True, null=True)
    assessed_by = models.CharField(max_length=400, blank=True, null=True)
    assessed_by_date = models.DateTimeField(blank=True, null=True)
    assessment_status = models.CharField(max_length=600, blank=True, null=True)
    status = models.CharField(max_length=800, blank=True, null=True)
    lastupdated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zsbt_capa_records_master'


class ZsbtMasterKpi(models.Model):
    kpi_id = models.BigAutoField(primary_key=True)
    graph_id = models.CharField(max_length=20, blank=True, null=True)
    kpi = models.CharField(max_length=400, blank=True, null=True)
    team_name = models.CharField(max_length=400, blank=True, null=True)
    kpi_type = models.CharField(max_length=200, blank=True, null=True)
    is_charter_kpi = models.CharField(max_length=100, blank=True, null=True)
    calc_logic = models.CharField(max_length=100, blank=True, null=True)
    unitforyaxis = models.CharField(max_length=100, blank=True, null=True)
    update_freq = models.CharField(max_length=100, blank=True, null=True)
    ttmonth = models.CharField(max_length=100, blank=True, null=True)
    ttyear = models.CharField(max_length=100, blank=True, null=True)
    lower_limit_w1 = models.CharField(max_length=100, blank=True, null=True)
    lower_limit_w2 = models.CharField(max_length=100, blank=True, null=True)
    lower_limit_w3 = models.CharField(max_length=100, blank=True, null=True)
    lower_limit_w4 = models.CharField(max_length=100, blank=True, null=True)
    upper_limit_w1 = models.CharField(max_length=100, blank=True, null=True)
    upper_limit_w2 = models.CharField(max_length=100, blank=True, null=True)
    upper_limit_w3 = models.CharField(max_length=100, blank=True, null=True)
    upper_limit_w4 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zsbt_master_kpi'


class ZsbtMasterMembers(models.Model):
    sno = models.BigAutoField(primary_key=True)
    team_name = models.CharField(max_length=400, blank=True, null=True)
    team_member = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zsbt_master_members'


class ZsbtMasterTeams(models.Model):
    team_id = models.BigAutoField(primary_key=True)
    end_time = models.CharField(max_length=255, blank=True, null=True)
    objective = models.CharField(max_length=255, blank=True, null=True)
    res_mdt = models.CharField(max_length=500, blank=True, null=True)
    shift = models.CharField(max_length=20, blank=True, null=True)
    start_time = models.CharField(max_length=255, blank=True, null=True)
    team_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zsbt_master_teams'


class ZsbtMdtEscalations(models.Model):
    esc_id = models.BigAutoField(primary_key=True)
    team_name = models.CharField(max_length=400, blank=True, null=True)
    escalation_date = models.DateTimeField(blank=True, null=True)
    shift = models.CharField(max_length=20, blank=True, null=True)
    sbt_mdt_escalation = models.CharField(max_length=600, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zsbt_mdt_escalations'


class ZsbtMeetingAgendaTable(models.Model):
    agenda_id = models.BigAutoField(primary_key=True)
    code_of_conduct = models.CharField(max_length=2000, blank=True, null=True)
    critical_for_24hr = models.CharField(max_length=2000, blank=True, null=True)
    agenda_date = models.DateTimeField(blank=True, null=True)
    desc_for_star_of_the_day = models.CharField(max_length=2000, blank=True, null=True)
    meeting_agenda = models.CharField(max_length=2000, blank=True, null=True)
    plan_for_day_1 = models.CharField(max_length=2000, blank=True, null=True)
    sbt_mdt_escalation = models.CharField(max_length=2000, blank=True, null=True)
    shift = models.CharField(max_length=20, blank=True, null=True)
    star_of_the_day = models.CharField(max_length=2000, blank=True, null=True)
    team_name = models.CharField(max_length=400, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zsbt_meeting_agenda_table'


class ZsbtShiftActive(models.Model):
    shift_active_id = models.BigAutoField(primary_key=True)
    active = models.CharField(max_length=10, blank=True, null=True)
    shift_date = models.DateTimeField(blank=True, null=True)
    shift = models.CharField(max_length=20, blank=True, null=True)
    team_name = models.CharField(max_length=400, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zsbt_shift_active'


class ZsbtShiftBased(models.Model):
    sno = models.BigAutoField(primary_key=True)
    team_name = models.CharField(max_length=400, blank=True, null=True)
    shift_source = models.CharField(max_length=10, blank=True, null=True)
    what = models.CharField(max_length=400, blank=True, null=True)
    creation_date = models.DateTimeField(blank=True, null=True)
    closure_date = models.DateTimeField(blank=True, null=True)
    who = models.CharField(max_length=400, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    comments = models.CharField(max_length=400, blank=True, null=True)
    status = models.CharField(max_length=400, blank=True, null=True)
    status_of_act = models.CharField(max_length=400, blank=True, null=True)
    assessment_status = models.CharField(max_length=400, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zsbt_shift_based'


class ZsbtStar(models.Model):
    star_id = models.BigAutoField(primary_key=True)
    teamname = models.CharField(max_length=400, blank=True, null=True)
    image_base = models.TextField(blank=True, null=True)
    upload_date = models.DateTimeField(blank=True, null=True)
    lastupdateddatetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zsbt_star'


class ZsbtTriggerHitCases(models.Model):
    trigger_id = models.BigAutoField(primary_key=True)
    kpi = models.CharField(max_length=400, blank=True, null=True)
    trigger_value = models.FloatField(blank=True, null=True)
    kpi_value = models.FloatField(blank=True, null=True)
    triggerd_date = models.DateTimeField(blank=True, null=True)
    ps_status = models.CharField(max_length=200, blank=True, null=True)
    team_name = models.CharField(max_length=400, blank=True, null=True)
    extracoulmn1 = models.CharField(max_length=200, blank=True, null=True)
    extracoulmn2 = models.CharField(max_length=200, blank=True, null=True)
    comments = models.CharField(max_length=400, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zsbt_trigger_hit_cases'
