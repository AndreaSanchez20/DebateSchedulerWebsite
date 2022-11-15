from django.db import models
import uuid
# Create your models here. models are classes that represent tables

class LoginAuth(models.Model):
    judgeId = models.CharField(max_length =20,null=False, blank=False)
    auth = models.BooleanField(null=False, blank=False)

    def __str__(self):
        return self.judgeId

class Note(models.Model):
    judgeId = models.CharField(max_length =20,null=False, blank=False)
    tournamentId = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    note = models.CharField(max_length =50,null=False, blank=False)

    def __str__(self):
        return self.note

class Tournament(models.Model):
    name = models.CharField(max_length =20,null=False, blank=False)
    tournamentId = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name

class Round(models.Model):
    team1 = models.CharField(max_length =3)
    school1 = models.CharField(max_length =20,null=False, blank=False)
    members1 = models.CharField(max_length =50,null=False, blank=False)
    position1 =  models.CharField(max_length =10,null=False, blank=False)
    team2 =  models.CharField(max_length =20,null=False, blank=False)
    school2 =  models.CharField(max_length =20,null=False, blank=False)
    members2 = models.CharField(max_length =50,null=False, blank=False)
    position2 =  models.CharField(max_length =20,null=False, blank=False)
    room =  models.CharField(max_length =3,null=False, blank=False)
    results =  models.CharField(max_length =20,null=False, blank=False)
    tournamentId = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    judgeId = models.CharField(max_length =20,null=False, blank=False)

    def __str__(self):
        return self.team1