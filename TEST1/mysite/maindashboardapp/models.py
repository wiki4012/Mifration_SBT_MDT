from django.conf import UserSettingsHolder
from django.db import models

# Create your models here.


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
    # Field renamed because it ended with '_'.
    when_field = models.CharField(
        db_column='when_', max_length=2000, blank=True, null=True)
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
    participants_names = models.CharField(
        max_length=400, blank=True, null=True)
    what = models.CharField(max_length=800, blank=True, null=True)
    where_s1 = models.CharField(max_length=800, blank=True, null=True)
    when_s1 = models.CharField(max_length=800, blank=True, null=True)
    who = models.CharField(max_length=800, blank=True, null=True)
    why = models.CharField(max_length=800, blank=True, null=True)
    howbig = models.CharField(max_length=800, blank=True, null=True)
    # This field type is a guess.
    evidance_links = models.TextField(blank=True, null=True)
    correction = models.CharField(max_length=600, blank=True, null=True)
    analyse_man = models.CharField(max_length=400, blank=True, null=True)
    analyse_method = models.CharField(max_length=400, blank=True, null=True)
    analyse_measurement = models.CharField(
        max_length=400, blank=True, null=True)
    analyse_machine = models.CharField(max_length=400, blank=True, null=True)
    analyse_material = models.CharField(max_length=400, blank=True, null=True)
    analyse_enviornment = models.CharField(
        max_length=400, blank=True, null=True)
    brainstorming_tool = models.CharField(
        max_length=400, blank=True, null=True)
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
    sbt_mdt_escalation = models.CharField(
        max_length=600, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zsbt_mdt_escalations'


class ZsbtMeetingAgendaTable(models.Model):
    agenda_id = models.BigAutoField(primary_key=True)
    code_of_conduct = models.CharField(max_length=2000, blank=True, null=True)
    critical_for_24hr = models.CharField(
        max_length=2000, blank=True, null=True)
    agenda_date = models.DateTimeField(blank=True, null=True)
    desc_for_star_of_the_day = models.CharField(
        max_length=2000, blank=True, null=True)
    meeting_agenda = models.CharField(max_length=2000, blank=True, null=True)
    plan_for_day_1 = models.CharField(max_length=2000, blank=True, null=True)
    sbt_mdt_escalation = models.CharField(
        max_length=2000, blank=True, null=True)
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
    extracolumn1 = models.CharField(max_length=200, blank=True, null=True)
    extracolumn2 = models.CharField(max_length=200, blank=True, null=True)
    comments = models.CharField(max_length=400, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zsbt_trigger_hit_cases'


