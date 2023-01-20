from django.db import models

class User(models.Model):
    user_id = models.CharField(max_length=32)
    #password = models.CharField(max_length=32)
    #email = models.CharField(max_length=64)
    scoreAll = models.IntegerField()
    card = models.IntegerField()


class Game(models.Model):
    hostUser= models.ForeignKey(User, on_delete=models.CASCADE, related_name="attack")
    guestUser= models.ForeignKey(User, on_delete=models.CASCADE, related_name="defense")
    result = models.CharField(max_length=8)
    winner = models.CharField(max_length=32)
    ing=models.BooleanField()
    standard=models.BooleanField() #높은쪽을 True
    score = models.IntegerField()
    accept = models.BooleanField()

