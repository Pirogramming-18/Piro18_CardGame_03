from django.db import models

class User(models.Model):
    userId = models.CharField(max_length=32)
    #password = models.CharField(max_length=32)
    #email = models.CharField(max_length=64)
    card = models.IntegerField()

class GestUser(models.Model):
    guestUser= models.ForeignKey(User, on_delete=models.CASCADE)
    
class Game(models.Model):
    hostUser= models.ForeignKey(User, on_delete=models.CASCADE)
    guestUser= models.ForeignKey(GestUser, on_delete=models.CASCADE)
    result = models.CharField(max_length=8)
    winner = models.CharField(max_length=32)
    ing=models.BooleanField()
    standard=models.BooleanField() #높은쪽을 True
    score = models.IntegerField()