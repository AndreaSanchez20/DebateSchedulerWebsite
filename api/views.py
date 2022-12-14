from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RoundSerializer
from .serializers import TournamentSerializer, LoginAuthSerializer, NoteSerializer
from debateApp.models import Round2,Note
from debateApp.models import Tournament, LoginAuth

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
            'team1':'team1aX',
            'school1':'school1a',
            'members1':'Andrea Sanchez, Paulina Hurtado',
            'position1': 'affirmative',
            'team2':'team2a',
            'school2':'school2a',
            'members2':'Ana Dogan, Hugh Mongus',
            'position2': 'negative',
            'room': '215B',
            'results': 'tbd',
            'tournamentId':'a691ad35-82e9-40a3-b635-632e5efb046e',
            'judgeId': 'judge1',
            'roundId':'r1',
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
            'tournamentId':'a691ad35-82e9-40a3-b635-632e5efb046e',
            'judgeId': 'judge2',
            'roundId':'r1',
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
            'judgeId': 'judge1',
            'roundId':'r1',
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
            'judgeId': 'judge2',
            'roundId':'r1',
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

    tournamentList = Tournament.objects.all()
    """tournamentList = [
    {
        'tournamentId':'1',
        'name': 'Lincoln Douglas'
    },
    {
        'tournamentId':'2',
        'name': 'Harvard'
    },
    ]
    """
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
    roundsList = Round2.objects.all().values()
    #print(roundsList)
    for item in roundsList:
        #round = Round.objects.get(id=tournamentId)
        if item['tournamentId']==tournamentId and item['judgeId']==judgeId:
            filteredRounds.append(item)
    #pass serialized data. books data converted from python to json
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

    noteList = Note.objects.filter(judgeId=judgeId,tournamentId=tournamentId).values()

    print(noteList)
    serializer= NoteSerializer(noteList, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def addNote(request, tournamentId, judgeId,note):
    currentNotes=[]
    item =	{'tournamentId':tournamentId,
            'judgeId': judgeId,
            'note': note
            }
    #adds item on currentNotes list.
    currentNotes.append(item)
    newNote = Note.objects.create(tournamentId=tournamentId,
            judgeId= judgeId,
            note= note)

    #fetches all current notes based on judge abd trournament id
    currentNotes = Note.objects.filter(judgeId=judgeId,tournamentId=tournamentId).values()

    print(currentNotes) #debugging
    serializer= NoteSerializer(currentNotes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getLogin(request, judgeId, password):
    result =	{'judgeId': judgeId,
            'auth': False
            }

    #check if password and judgeId is on the list and change auth property if so
    for item in userList:
        if item['password']==password and item['judgeId']==judgeId:
            result['auth'] = True

    print(result)
    serializer= LoginAuthSerializer(result)
    return Response(serializer.data)

@api_view(['GET'])
def deleteNote(request, tournamentId, judgeId,noteId):
    currentNotes=[]

    note = Note.objects.get(noteId=noteId)
    #debugging
    print("NOTEID: " + noteId)
    note.delete() #deletes object

    #brings notes based on the signed in judge and trounament chosen
    currentNotes = Note.objects.filter(judgeId=judgeId,tournamentId=tournamentId).values()

    serializer= NoteSerializer(currentNotes, many=True)
    return Response(serializer.data)
