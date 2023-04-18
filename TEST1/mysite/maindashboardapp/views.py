from django.shortcuts import render
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *
from htmls import *
from django.http import HttpResponse


def main_dashboard(request):
    return render(request, "main_dashboard_index.html")


def cockpit_1(request):
    return render(request, "cockpit_1_index.html")


def monthly(request):
    return render(request, "monthly_index.html")


def cockpit_2(request):
    return render(request, "cockpit_2_index.html")


def daily(request):
    return render(request, "daily_index.html")


def analysis(request):
    return render(request, "analysis_index.html")


def capa(request):
    return render(request, "capa_index.html")

# TEAMS_NAME.l


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/task-list/',
        'Detail View': '/task-detail/<str:pk>/',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/',
    }

    return Response(api_urls)

#  COCKPIT_1


@api_view(['GET'])
def taskList(request):
    tasks = ZsbtMasterTeams.objects.all().order_by('-team_id')
    serializer = ZsbtMasterTeamsSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getTeamMembers(request):
    print("hi")
    searchWord = request.GET.get('team')
    print("searchWord", searchWord)
    tasks = ZsbtMasterMembers.objects.all().filter(team_name=searchWord).values()
    print(tasks)
    # tasks = ZsbtMasterTeams.objects.raw("SELECT * FROM main_dashboard_app;")
    serializer = ZsbtMasterMembersSerializer(tasks, many=True)
    # return HttpResponse(request,{'tasks':tasks})
    return Response(serializer.data)
    # return HttpResponse(searchWord)


# TRRIGER_HIT_CASES.
# @api_view(['GET'])
# def triggerHitCases(request):
#     tasks = ZsbtMasterTeams.objects.all().filter(shift='A').values()
#     # tasks = ZsbtMasterTeams.objects.raw("SELECT * FROM main_dashboard_app;")
#     serializer = ZsbtMasterTeamsSerializer(tasks, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# @renderer_classes((TemplateHTMLRenderer, JSONRenderer))
# def triggerHitCases(request):
# #     temp = "SBT - Fast and Furious"
# #     tasks = ZsbtTriggerHitCases.objects.all().filter(team_name=temp,ps_status = 'Created').values()
#     # val = "maindashboardapp_ZsbtTriggerHitCases"
#     tasks = ZsbtTriggerHitCases.objects.raw("select * from  maindashboardapp_ZsbtTriggerHitCases")
#     # serializer = ZsbtTriggerHitCasesSerializer(tasks, many=True)
#     # return Response(serializer.data)
#     print(request)
#     return render(request,template_name='main_dashboard_index.html')

@api_view(['GET'])
def triggerHitCases(request):
    temp = "SBT - Fast and Furious"
    # tasks = ZsbtTriggerHitCases.objects.all().filter(team_name=temp,ps_status = 'Created').values()
    tasks = ZsbtMasterTeams.objects.raw(
        "SELECT * FROM zsbt_master_teams where team_name = 'SBT - Extreme Warriors'")
    serializer = ZsbtTriggerHitCasesSerializer(tasks, many=True)
    return Response(serializer.data)

# Main_Dashboard


@api_view(['GET'])
def getMeetingAgenda(request):
    print("hi_mian")
    searchWord = request.GET.get('team')
    print("searchWord", searchWord)
    # tasks = ZsbtMeetingAgendaTable.objects.all().filter(team_name=searchWord).values()
    tasks = ZsbtMeetingAgendaTable.objects.raw(
        "select * from zsbt_meeting_agenda_table where team_name = %s order by agenda_date desc", [searchWord])
    print(tasks)
    serializer = ZsbtMeetingAgendaTableSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getShiftWiseMember(request):
    print("hi_mian")
    searchWord = request.GET.get('team')
    print("searchWord", searchWord)
    # tasks = ZsbtMeetingAgendaTable.objects.all().filter(team_name=searchWord).values()
    tasks = ZsbtAttendance.objects.raw(
        "select TEAM_MEMBER,ATTENDANCE,from ZSBT_ATTENDANCE where TEAM_NAME ='team_name' and SHIFT ='shift' and DATE ='date'")
    print(tasks)
    serializer = ZsbtAttendanceSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getKpiDaily(request):
    print("hi_mian")
    team = request.GET.get('team')
    fromDa = request.GET.get('from')
    toDa = request.GET.get('to')
    fromDate = fromDa[:10]
    toDate = toDa[:10]
    # team = 'MDT - Production Pioneers'
    # fromDate = "2022-03-01"
    # toDate = "2023-04-16"

    print("PArams", team, fromDate, toDate)
    # searchWord = request.GET.get('team')
    # print("searchWord",searchWord)
    # tasks = ZsbtMeetingAgendaTable.objects.all().filter(team_name=searchWord).values()
    # tasks = ZkpiManualDate.objects.raw("select MANNUAL_KPI_ID,kpi_name from ZKPI_MANUAL_DATE ")
    tasks = ZkpiManualDate.objects.raw(
        "select * FROM ZKPI_MANUAL_DATE where KPI_DATE between '{0}' and '{1}' and team_name = '{2}' ".format(fromDate, toDate, team))
    # tasks = ZkpiManualDate.objects.raw("SELECT * FROM ZKPI_MANUAL_DATE where KPI_DATE>='01-01-2023' and KPI_DATE <='21-01-2023' and TEAM_NAME = 'MDT - Production Pioneers' order by graph_id,kpi_date FETCH NEXT 10 ROWS ONLY")
    print('hitttttttttt', tasks)
    serializer = ZkpiManualDateSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getKpiByMonth(request):
    print("hi_mian")
    team = request.GET.get('team')
    fromMon = request.GET.get('fromMon')
    fromYear = request.GET.get('fromYear')
    toMon = request.GET.get('toMon')
    toYear = request.GET.get('toYear')
    # searchWord = request.GET.get('team')
    # print("searchWord",searchWord)
    # tasks = ZsbtMeetingAgendaTable.objects.all().filter(team_name=searchWord).values()
    # tasks = ZkpiManualDate.objects.raw("select MANNUAL_KPI_ID,kpi_name from ZKPI_MANUAL_DATE ")
    tasks = ZsbtMasterKpi.objects.raw(
        "SELECT * FROM ZSBT_MASTER_KPI WHERE TEAM_NAME = '{0}' and TTMONTH between '{1}' and '{2}' and TTYEAR between '{3}' and '{4}' ORDER BY GRAPH_ID".format(team, fromMon, toMon, toYear, fromYear))
    # tasks = ZkpiManualDate.objects.raw("SELECT * FROM ZKPI_MANUAL_DATE where KPI_DATE>='01-01-2023' and KPI_DATE <='21-01-2023' and TEAM_NAME = 'MDT - Production Pioneers' order by graph_id,kpi_date FETCH NEXT 10 ROWS ONLY")
    print('hittt', tasks)
    serializer = ZsbtMasterKpiSerializer(tasks, many=True)
    return Response(serializer.data)


# MONTHLY

@api_view(['GET'])
def getKpiMonthly(request):
    print("hi_mian")
    # team = request.GET.get('team')
    team = "MDT - House of Guardians"
    # print("PArams", team)
    tasks = ZkpiManualDate.objects.raw("select MANNUAL_KPI_ID,GRAPH_ID,KPI_NAME AS KPI,to_char(cast(kpi_date as date),'MM') AS MONTH,to_char(cast(kpi_date as date),'YYYY') AS YEAR,KPI_DATE from(SELECT MANNUAL_KPI_ID,GRAPH_ID,KPI_NAME,to_char(cast(kpi_date as date),'MM') AS MONTH,to_char(cast(kpi_date as date),'YYYY') AS YEAR,KPI_DATE,row_number() OVER(PARTITION BY A.graph_id, to_char(cast(A.kpi_date as date),'MM'), to_char(cast(A.kpi_date as date),'YYYY') ORDER BY (A.KPI_DATE) DESC) AS rn from ZKPI_MANUAL_DATE A WHERE kpi_name is not null and A.TEAM_NAME = %s and to_char(cast(KPI_DATE as date),'yyyy-mm-dd') >= CONCAT(substr(TO_CHAR(ADD_MONTHS(to_char(cast(SYSTIMESTAMP as date)), -23), 'YYYY-MM-dd'),0,7),'-01T00:00:00') AND to_char(cast(KPI_DATE as date),'yyyy-mm-dd')<=to_char(cast(SYSTIMESTAMP as date),'yyyy-mm-dd')GROUP BY to_char(cast(kpi_date as date),'MM'), to_char(cast(kpi_date as date),'YYYY'), MANNUAL_KPI_ID,KPI_NAME,GRAPH_ID, KPI_DATE ORDER BY  GRAPH_ID ,to_char(cast(kpi_date as date),'YYYY') DESC,to_char(cast(kpi_date as date),'MM') DESC)WHERE rn=1",[team])
    # print('MONTHLY_nn',tasks)

    serializer = ZkpiManualDateSerializer(tasks, many=True)
  
    return Response(serializer.data)

@api_view(['GET'])
def getKpiMonthlyUnion(request):
    print("hi_mian")
    # team = request.GET.get('team')
    team = "MDT - House of Guardians"
    graphId = "5"
    ttMon = "11"
    ttYear = "2022"
    # print("PArams", team)
    tasks = ZsbtMasterKpi.objects.raw("select MANNUAL_KPI_ID,GRAPH_ID,KPI_NAME AS KPI,to_char(cast(kpi_date as date),'MM') AS MONTH,to_char(cast(kpi_date as date),'YYYY') AS YEAR,KPI_DATE from(SELECT MANNUAL_KPI_ID,GRAPH_ID,KPI_NAME,to_char(cast(kpi_date as date),'MM') AS MONTH,to_char(cast(kpi_date as date),'YYYY') AS YEAR,KPI_DATE,row_number() OVER(PARTITION BY A.graph_id, to_char(cast(A.kpi_date as date),'MM'), to_char(cast(A.kpi_date as date),'YYYY') ORDER BY (A.KPI_DATE) DESC) AS rn from ZKPI_MANUAL_DATE A WHERE kpi_name is not null and A.TEAM_NAME = %s and to_char(cast(KPI_DATE as date),'yyyy-mm-dd') >= CONCAT(substr(TO_CHAR(ADD_MONTHS(to_char(cast(SYSTIMESTAMP as date)), -23), 'YYYY-MM-dd'),0,7),'-01T00:00:00') AND to_char(cast(KPI_DATE as date),'yyyy-mm-dd')<=to_char(cast(SYSTIMESTAMP as date),'yyyy-mm-dd')GROUP BY to_char(cast(kpi_date as date),'MM'), to_char(cast(kpi_date as date),'YYYY'), MANNUAL_KPI_ID,KPI_NAME,GRAPH_ID, KPI_DATE ORDER BY  GRAPH_ID ,to_char(cast(kpi_date as date),'YYYY') DESC,to_char(cast(kpi_date as date),'MM') DESC)WHERE rn=1",[team])
    # print('MONTHLY_nn',tasks)
    tasks2 = ZsbtMasterKpi.objects.raw(
        "SELECT * FROM ZSBT_MASTER_KPI WHERE TEAM_NAME = '{0}' and TTMONTH ='{1}' and TTYEAR = '{2}' and graph_id = '{3}' ORDER BY GRAPH_ID".format(team, ttMon, ttYear,graphId))
    # print('MONTHLY_nn',tasks)
  
    serializer1 = ZkpiManualDateSerializer(tasks, many=True)
    serializer2 = ZsbtMasterKpiSerializer(tasks2, many=True)
    model_combination = ZsbtMasterKpi.union(ZsbtMasterKpi, all=True)
    print("--------------",model_combination)
    return Response(model_combination.data)

@api_view(['GET'])
def getTTbyMonth(request):
    print("hi_mian")
    # team = request.GET.get('team')
    # graphId = request.GET.get('graphId')
    # ttMon = request.GET.get('ttMon')
    # ttYear = request.GET.get('ttYear')
    team = "MDT - House of Guardians"
    graphId = "5"
    ttMon = "11"
    ttYear = "2022"
    print("parameters",team,graphId,ttMon,ttYear)
    # searchWord = request.GET.get('team')
    # print("searchWord",searchWord)
    # tasks = ZsbtMeetingAgendaTable.objects.all().filter(team_name=searchWord).values()
    # tasks = ZkpiManualDate.objects.raw("select MANNUAL_KPI_ID,kpi_name from ZKPI_MANUAL_DATE ")
    tasks = ZsbtMasterKpi.objects.raw(
        "SELECT * FROM ZSBT_MASTER_KPI WHERE TEAM_NAME = '{0}' and TTMONTH ='{1}' and TTYEAR = '{2}' and graph_id = '{3}' ORDER BY GRAPH_ID".format(team, ttMon, ttYear,graphId))
    # tasks = ZkpiManualDate.objects.raw("SELECT * FROM ZKPI_MANUAL_DATE where KPI_DATE>='01-01-2023' and KPI_DATE <='21-01-2023' and TEAM_NAME = 'MDT - Production Pioneers' order by graph_id,kpi_date FETCH NEXT 10 ROWS ONLY")
    print('hittt', tasks)
    serializer = ZsbtMasterKpiSerializer(tasks, many=True)
    return Response(serializer.data)


#COCKPIT_2

@api_view(['GET'])
def getKpiCockpit_2(request):
    print("hi_mian")
    team = request.GET.get('team')
    date = request.GET.get('date')
    # date = "2022-11-02"
    # team = "MDT - House of Guardians"
    print("PArams", team)
    tasks = ZkpiManualDate.objects.raw(
        "select distinct KPI_NAME, ZKPI_MANUAL_DATE.* from ZKPI_MANUAL_DATE where TEAM_NAME = '{0}' and to_char(cast(KPI_DATE as date),'yyyy-mm-dd') ='{1}' order by graph_id".format(team,date))
    print('MONTHLY_nn',tasks)
    serializer = ZkpiManualDateSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getCurrentKpiCockpit_2(request):
    print("hi_mian")
    team = request.GET.get('team')
    ttMon = request.GET.get('ttMon')
    ttYear = request.GET.get('ttYear')
    print("parameters",team,ttMon,ttYear)
    tasks = ZsbtMasterKpi.objects.raw(
        "SELECT * FROM ZSBT_MASTER_KPI  WHERE TEAM_NAME = '{0}' and TTMONTH like '{1}' and TTYEAR = '{2}'".format(team,ttMon,ttYear))
    # tasks = ZkpiManualDate.objects.raw("SELECT * FROM ZKPI_MANUAL_DATE where KPI_DATE>='01-01-2023' and KPI_DATE <='21-01-2023' and TEAM_NAME = 'MDT - Production Pioneers' order by graph_id,kpi_date FETCH NEXT 10 ROWS ONLY")
    print('hittt', tasks)
    serializer = ZsbtMasterKpiSerializer(tasks, many=True)
    return Response(serializer.data)