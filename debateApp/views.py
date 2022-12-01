import requests

from ast import For
from django.shortcuts import render
from http.client import HTTPResponse
from django.http import HttpResponse

import json

#from django.http import HttpResponse
#from django.template import loader
# Create your views here.
from pathlib import Path
baseURL= ""#request.build_absolute_uri() 
#request.META['HTTP_HOST'] #request.get_full_path() #getCurrent()
#BASE_DIR = Path(__file__).resolve().parent.parent
#request.build_absolute_uri()

def index(request):
    #calls the API that returns tournaments data 
    print(request.META['HTTP_HOST'])
    print("HOST:")
    print(request.build_absolute_uri())
    response = requests.get(request.build_absolute_uri("/api/tournament"))
    #loads data as JSON
    tournamentListAPI = json.loads(response.text)

    responseQuote = requests.get('https://favqs.com/api/qotd')
    quoteAPI = json.loads(responseQuote.text) # Check the JSON Response Content documentation below

    #sends data in context
    context ={'tournaments':tournamentListAPI, 'quote':quoteAPI}
    print(context)

    return render(request, 'debateApp/index.html', context)

def dashboard(request):
    response = requests.get(request.build_absolute_uri("/api/tournament"))
    tournamentListAPI = json.loads(response.text)
    
    context ={'tournaments':tournamentListAPI, 'dashboard':None}
    return render(request, 'debateApp/dashboard.html', context)


def dashboardbyTournament(request, tournamentId):
    response = requests.get(request.build_absolute_uri("/api/tournament"))
    tournamentListAPI = json.loads(response.text)
    
    response = requests.get(request.build_absolute_uri("/api/dashboard/"+tournamentId))
    dashboardListAPI = json.loads(response.text)
    
    context ={'tournaments':tournamentListAPI, 'dashboard':dashboardListAPI}
    return render(request, 'debateApp/dashboard.html', context)

def dashboardUpdated(request, tournamentId,judgeId, result):
    #updates dashboard
    response = requests.post(request.build_absolute_uri("/api/dashboardUpdate/"+tournamentId+ "/" + judgeId + "/" +result))
    #loads and displays updated dashboard

    return dashboardbyTournament(request, tournamentId)


def about(request):
    context={}
    return render(request, 'debateApp/about.html', context)

def judgeBallot(request,tournamentId, judgeId):
    response = requests.get(request.build_absolute_uri("/api/judgeRound/" + tournamentId + '/'+ judgeId  ))
    tournamentListAPI = json.loads(response.text)
    #TODO: add prev notes api
    response = requests.get(request.build_absolute_uri("/api/judgeBallotNotes/" + tournamentId + '/'+ judgeId ))

    noteListAPI = json.loads(response.text)

    context ={'round':tournamentListAPI, 'notes': noteListAPI}
    return render(request, 'debateApp/judge-ballot.html', context)

def judgeBallot2(request,tournamentId, judgeId):
    context ={'tournamentId':tournamentId, 'judgeId':judgeId}
    return render(request, 'debateApp/judge-ballot-2.html', context)

def judgeRound(request, tournamentId, judgeId):
    response = requests.get(request.build_absolute_uri("/api/judgeRound/" + tournamentId + '/'+ judgeId  ))
    tournamentListAPI = json.loads(response.text)
    context ={'round':tournamentListAPI}
    print(context)
    return render(request, 'debateApp/judge-round.html', context)

def studentRound(request, tournamentId):
    response = requests.get(request.build_absolute_uri("/api/judgeRound/" + tournamentId  ))
    tournamentListAPI = json.loads(response.text)
    context ={'round':tournamentListAPI}
    print(context)
    return render(request, 'debateApp/student-round.html', context)

def addNote(request, tournamentId, judgeId, note):
    response = requests.get(request.build_absolute_uri("/api/judgeBallotNotes/" + tournamentId + '/'+ judgeId +"/"+note ))
    notesListAPI = json.loads(response.text)

    response = requests.get(request.build_absolute_uri("/api/judgeRound/" + tournamentId + '/'+ judgeId  ))
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