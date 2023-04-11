from django.shortcuts import render
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *


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


@api_view(['GET'])
def taskList(request):
    tasks = ZsbtMasterTeams.objects.all().order_by('-team_id')
    serializer = ZsbtMasterTeamsSerializer(tasks, many=True)
    return Response(serializer.data)


# TRRIGER_HIT_CASES.
# @api_view(['GET'])
# def triggerHitCases(request):
#     tasks = ZsbtMasterTeams.objects.all().filter(shift='A').values()
#     # tasks = ZsbtMasterTeams.objects.raw("SELECT * FROM main_dashboard_app;")
#     serializer = ZsbtMasterTeamsSerializer(tasks, many=True)
#     return Response(serializer.data)

@api_view(['GET'])
def triggerHitCases(request):
#     temp = "SBT - Fast and Furious"
#     tasks = ZsbtTriggerHitCases.objects.all().filter(team_name=temp,ps_status = 'Created').values()
    tasks = ZsbtTriggerHitCases.objects.raw("SELECT * FROM main_dashboard_app_ZsbtTriggerHitCases")
    for p in tasks:
        print(p)
      
    serializer = ZsbtTriggerHitCasesSerializer(tasks, many=True)
    return Response(serializer.data)

# @api_view(['GET'])
# def triggerHitCases(request):
#     temp = "SBT - Fast and Furious"
#     tasks = ZsbtTriggerHitCases.objects.all().filter(team_name=temp,ps_status = 'Created').values()
#     # tasks = ZsbtMasterTeams.objects.raw("SELECT * FROM main_dashboard_app;")
#     serializer = ZsbtTriggerHitCasesSerializer(tasks, many=True)
    # return Response(serializer.data)

