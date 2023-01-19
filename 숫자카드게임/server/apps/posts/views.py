from django.shortcuts import render, redirect
from django.http.request import HttpRequest

from models import Game, User

from random import randint

# Create your views here.

#make five random cards
def makeCard(request, pk, *args, **kwargs):
  
  cardList = []
  user =User.objects.get(id=pk)
  for i in range(5): #make five integers
    card = randint(1, 10)
    while card in cardList: #not for overlapping
      card = randint(1, 10)
    cardList.append(card)
  print(cardList)
  
  user.cardList = cardList
  return render(request, "game/attack.html")


def showstate(request, pk, *args, **kwargs):
    game = Game.objects.get(id = pk)
    hostCard = game.hostUser.card
    guestCard = game.guestUser.card
    if hostCard is not None and guestCard is None: # 게임 진행중..
        ing = True  #list.html 에서 ing를 받아옴
    elif hostCard is None and guestCard is not None: # 반격하기
        ing= False  #list.html 에서 ing을 받아옴


    
