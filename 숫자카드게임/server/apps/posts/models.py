from django.db import models

class User(models.Model):
    id = models.CharField(max_length=32 ,primary_key=True)
    #password = models.CharField(max_length=32)
    #email = models.CharField(max_length=64)
    scoreAll = models.IntegerField()
    card = models.IntegerField()

    guestUser= models.ForeignKey(User, on_delete=models.CASCADE,primary_key=True)
class Game(models.Model):
    hostUser= models.ForeignKey(User, on_delete=models.CASCADE)
    guestUser= models.ForeignKey(GestUser, on_delete=models.CASCADE)
    result = models.CharField(max_length=8,null=True)
    winner = models.CharField(max_length=32,null=True)
    ing=models.BooleanField()
    standard=models.BooleanField() #높은쪽을 True
    score = models.IntegerField()