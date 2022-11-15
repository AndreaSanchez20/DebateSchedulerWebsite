from django.http import HttpResponse
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/<str:tournamentId>', views.dashboardbyTournament, name='dashboardbyTournament'),
    path('dashboard/<str:tournamentId>/<str:judgeId>/<str:result>', views.dashboardUpdated, name='dashboardUpdated'),
    path('student-round/', views.studentRound, name='student-round'),
    path('about', views.about, name='about'),
    path('judge-round/<str:tournamentId>/<str:judgeId>', views.judgeRound, name='judge-round'),
    path('judge-ballot/<str:tournamentId>/<str:judgeId>/<str:note>', views.addNote, name='judge-ballot-notes'),
    path('judge-ballot/<str:tournamentId>/<str:judgeId>', views.judgeBallot, name='judge-ballot-current-notes'),
    path('judge-sign-in/<str:tournamentId>', views.judgeSignIn, name='judge-sign-in'),
    path('judge-ballot-2/<str:tournamentId>/<str:judgeId>', views.judgeBallot2, name='judge-ballot-2'),
]