"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from maindashboardapp import views 
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('main_dashboard', views.main_dashboard),
    path('cockpit_1', views.cockpit_1),
    path('cockpit_2', views.cockpit_2),
    path('capa', views.capa),
    path('analysis', views.analysis),
    path('daily', views.daily),
    path('monthly', views.monthly),
    path('', views.apiOverview, name="api-overview"),
    path('task-list', views.taskList, name="task-list"),
    path('trigger-hit-list', views.triggerHitCases, name="trigger-hit-list"),
    path('get-team-members', views.getTeamMembers, name="get-team-members"),
    path('get-meeting-agenda', views.getMeetingAgenda, name="get-meeting-agenda"),
    path('get-KpiDaily', views.getKpiDaily, name="get-KpiDaily"),
    path('get-KpiByMonth', views.getKpiByMonth, name="get-KpiByMonth"),
    path('get-KpiMonthlyKpi', views.getKpiMonthly, name="get-KpiMonthlyKpi"),
    path('get-TTMonthlyKpi', views.getTTbyMonth, name="get-TTMonthlyKpi"),
    path('get-kpiCockpit_2', views.getKpiCockpit_2, name="get-kpiCockpit_2"),
    path('get-kpiCurrentCockpit_2', views.getCurrentKpiCockpit_2, name="get-kpiCurrentCockpit_2"),
    path('get-attDump', views.getAttDump, name="get-attDump"),
    path('get-capaDump', views.getCapaDump, name="get-capaDump"),
    path('get-kpiUnion', views.getKpiMonthlyUnion, name="get-kpiUnion"),
    path('get-export', views.export, name="get-export"),
    path('get-ProblemSolving', views.getProblemSolving, name="get-ProblemSolving"),
    path('get-Actionables', views.getActionables, name="get-Actionables"),
        
] 