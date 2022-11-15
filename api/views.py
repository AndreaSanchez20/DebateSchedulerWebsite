from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RoundSerializer
from .serializers import TournamentSerializer, NotesSerializer, LoginAuthSerializer
from debateApp.models import Round
from debateApp.models import Tournament, Note, LoginAuth

#API data as dictionaries
userList = [
        {
            'judgeId':'judge1',
            'password': '248'
        },
        {
            'judgeId':'judge2',
            'password': '248'
        }
        ]

noteList = [
        {
            'tournamentId':'9999',
            'judgeId': '',
            'note': ''
        }]

roundsList = [
        {
            'team1':'team1a',
            'school1':'school1a',
            'members1':'Andrea Sanchez, Paulina Hurtado',
            'position1': 'affirmative',
            'team2':'team2a',
            'school2':'school2a',
            'members2':'Ana Dogan, Hugh Mongus',
            'position2': 'negative',
            'room': '215B',
            'results': 'tbd',
            'tournamentId':'1',
            'judgeId': 'judge1'
        },
        {
            'team1':'team1b',
            'school1':'school1b',
            'members1':'Alex Sanchez2, Paulina Hurtado2',
            'position1': 'affirmative',
            'team2':'team2b',
            'school2':'school2b',
            'members2':'Paola Dogan2, Hugh Mongus2',
            'position2': 'negative',
            'room': '2',
            'results': 'tbd',
            'tournamentId':'1',
            'judgeId': 'judge2'
        },
        {
            'team1':'team3a',
            'school1':'school3a',
            'members1':'Andrea Sanchez3, Paulina Hurtado3',
            'position1': 'affirmative',
            'team2':'team4a',
            'school2':'school4a',
            'members2':'Ana Dogan3, Hugh Mongus3',
            'position2': 'negative',
            'room': '3',
            'results': 'tbd',
            'tournamentId':'2',
            'judgeId': 'judge1'
        },
        {
            'team1':'team3b',
            'school1':'school3b',
            'members1':'Andrea Sanchez4, Paulina Hurtado4',
            'position1': 'affirmative',
            'team2':'team4b',
            'school2':'school4b',
            'members2':'Ana Dogan4, Hugh Mongus4',
            'position2': 'negative',
            'room': '4',
            'results': 'tbd',
            'tournamentId':'2',
            'judgeId': 'judge2'
        }
    ]

#Test API
@api_view(['GET'])
def getRoutes(request):
#routes is made up of a list of dictionaries which will be converted to JS lists
    routes = [
        {'GET': '/api/dashboard'},
        {'GET': '/api/tournament'},
    ]

    return Response(routes)
    #safe turns data into JSON data. 

#Tournaments API data for main page combo box
@api_view(['GET'])
def getTournament(request):
    #tournament = Tournament.objects.all()
    #pass serialized data. books data converted from python to json

    tournamentList = [
    {
        'tournamentId':'1',
        'name': 'Lincoln Douglas'
    },
    {
        'tournamentId':'2',
        'name': 'Harvard'
    },
    ]
    #serialize data to send
    serializer= TournamentSerializer(tournamentList, many=True)
    #returns serialized data
    return Response(serializer.data)

#sends dashboard data
@api_view(['GET'])
def getDashboard(request, tournamentId):
    #round = Round.objects.all()

    #get only rounds based on the tournament chosen
    filteredRounds=[]
    for item in roundsList:
        if item['tournamentId']==tournamentId:
            filteredRounds.append(item)

    serializer= RoundSerializer(filteredRounds, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getJudgeRound(request, tournamentId, judgeId):
    filteredRounds=[]
    for item in roundsList:
        if item['tournamentId']==tournamentId and item['judgeId']==judgeId:
            filteredRounds.append(item)

    serializer= RoundSerializer(filteredRounds, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def getRoundsUpdated(request, tournamentId,judgeId, result):
    for item in roundsList:
        if item['tournamentId']==tournamentId and item['judgeId']==judgeId:
            item['results'] = result
    serializer= RoundSerializer(roundsList, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getNote(request, tournamentId, judgeId):
    currentNotes=[]
    item =	{'tournamentId':"",
            'judgeId': "",
            'note': ""
            }
    currentNotes.append(item)

    for item in noteList:
        if item['tournamentId']==tournamentId and item['judgeId']==judgeId:
            currentNotes.append(item)

    #filteredRounds = roundsList.object.filter(id=tournamentId)
    print(currentNotes)
    serializer= NotesSerializer(currentNotes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def addNote(request, tournamentId, judgeId,note):
    currentNotes=[]
    item =	{'tournamentId':tournamentId,
            'judgeId': judgeId,
            'note': note
            }
    currentNotes.append(item)
    for i in noteList:
        print("in for")
        print(noteList)
        if i['tournamentId']==tournamentId and i['judgeId']==judgeId:
            currentNotes.append(i)
    noteList.append(item)
    print("out for")
    print(currentNotes)
    serializer= NotesSerializer(currentNotes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getLogin(request, judgeId, password):
    result =	{'judgeId': judgeId,
            'auth': False
            }

    for item in userList:
        if item['password']==password and item['judgeId']==judgeId:
            result['auth'] = True

    print(result)
    serializer= LoginAuthSerializer(result)
    return Response(serializer.data)
