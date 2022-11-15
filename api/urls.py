from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('tournament/', views.getTournament),
    path('dashboard/', views.getDashboard),
    path('dashboard/<str:tournamentId>', views.getDashboard),
    path('dashboard/<str:tournamentId>/update/', views.getRoundsUpdated),
    path('judgeRound/<str:tournamentId>/<str:judgeId>', views.getJudgeRound),
    path('judgeBallotNotes/<str:tournamentId>/<str:judgeId>', views.getNote),
    path('judgeBallotNotes/<str:tournamentId>/<str:judgeId>/<str:note>', views.addNote),
    path('dashboardUpdate/<str:tournamentId>/<str:judgeId>/<str:result>', views.getRoundsUpdated),
    path('judgeLogin/<str:judgeId>/<str:password>', views.getLogin),
]