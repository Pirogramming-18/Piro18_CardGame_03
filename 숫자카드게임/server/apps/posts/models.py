from django.db import models

class User(models.Model):
    user_id = models.CharField(max_length=32, primary_key=True)
    #password = models.CharField(max_length=32)
    #email = models.CharField(max_length=64)
    scoreAll = models.IntegerField()
    cardList = []
    
class Game(models.Model):
    hostUser= models.ForeignKey(User, on_delete=models.CASCADE)
    guestUser= models.ForeignKey(User, on_delete=models.CASCADE)
    result = models.CharField(max_length=8)
    winner = models.CharField(max_length=32)
    ing=models.BooleanField()
    standard=models.BooleanField() #높은쪽을 True
    score = models.IntegerField()