import requests

from ast import For
from django.shortcuts import render
from http.client import HTTPResponse
from django.http import HttpResponse

import json

#from django.http import HttpResponse
#from django.template import loader
# Create your views here.

def index(request):
    #calls the API that returns tournaments data 
    response = requests.get("http://127.0.0.1:8000/api/tournament")
    #loads data as JSON
    tournamentListAPI = json.loads(response.text)
    #sends data in context
    context ={'tournaments':tournamentListAPI}
    print(context)
    return render(request, 'debateApp/index.html', context)

def dashboard(request):
    response = requests.get("http://127.0.0.1:8000/api/tournament")
    tournamentListAPI = json.loads(response.text)
    
    context ={'tournaments':tournamentListAPI, 'dashboard':None}
    return render(request, 'debateApp/dashboard.html', context)


def dashboardbyTournament(request, tournamentId):
    response = requests.get("http://127.0.0.1:8000/api/tournament")
    tournamentListAPI = json.loads(response.text)
    
    response = requests.get("http://127.0.0.1:8000/api/dashboard/"+tournamentId)
    dashboardListAPI = json.loads(response.text)
    
    context ={'tournaments':tournamentListAPI, 'dashboard':dashboardListAPI}
    return render(request, 'debateApp/dashboard.html', context)

def dashboardUpdated(request, tournamentId,judgeId, result):
    #updates dashboard
    response = requests.post("http://127.0.0.1:8000/api/dashboardUpdate/"+tournamentId+ "/" + judgeId + "/" +result)
    #loads and displays updated dashboard

    return dashboardbyTournament(request, tournamentId)


def about(request):
    context={}
    return render(request, 'debateApp/about.html', context)

def judgeBallot(request,tournamentId, judgeId):
    response = requests.get("http://127.0.0.1:8000/api/judgeRound/" + tournamentId + '/'+ judgeId  )
    tournamentListAPI = json.loads(response.text)
    #TODO: add prev notes api
    response = requests.get("http://127.0.0.1:8000/api/judgeBallotNotes/" + tournamentId + '/'+ judgeId )

    noteListAPI = json.loads(response.text)

    context ={'round':tournamentListAPI, 'notes': noteListAPI}
    return render(request, 'debateApp/judge-ballot.html', context)

def judgeBallot2(request,tournamentId, judgeId):
    context ={'tournamentId':tournamentId, 'judgeId':judgeId}
    return render(request, 'debateApp/judge-ballot-2.html', context)

def judgeRound(request, tournamentId, judgeId):
    response = requests.get("http://127.0.0.1:8000/api/judgeRound/" + tournamentId + '/'+ judgeId  )
    tournamentListAPI = json.loads(response.text)
    context ={'round':tournamentListAPI}
    print(context)
    return render(request, 'debateApp/judge-round.html', context)

def studentRound(request, tournamentId):
    response = requests.get("http://127.0.0.1:8000/api/judgeRound/" + tournamentId  )
    tournamentListAPI = json.loads(response.text)
    context ={'round':tournamentListAPI}
    print(context)
    return render(request, 'debateApp/student-round.html', context)

def addNote(request, tournamentId, judgeId, note):
    response = requests.get("http://127.0.0.1:8000/api/judgeBallotNotes/" + tournamentId + '/'+ judgeId +"/"+note )
    notesListAPI = json.loads(response.text)

    response = requests.get("http://127.0.0.1:8000/api/judgeRound/" + tournamentId + '/'+ judgeId  )
    tournamentListAPI = json.loads(response.text)
    context ={'round':tournamentListAPI, 'notes': notesListAPI}
    #print(context)
    return render(request, 'debateApp/judge-ballot.html', context)

def judgeSignIn(request, tournamentId):
    context ={'tournamentId':tournamentId}
    return render(request,'debateApp/judge-sign-in.html', context)
#Loading: consists of finding the template for a given indentifier and preprocessing it, usually compiling it to an in-memory representation
#rendering: interpolating the template with context data and returning the resulting string. replaces vars wit their values which are looked up in the context and executes tags. everyhting else is output as is
#template system uses dot-lookup syntax to access var attributes