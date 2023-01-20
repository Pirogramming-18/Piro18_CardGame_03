from django.shortcuts import render, redirect
from django.http.request import HttpRequest

from server.apps.posts.models import Game, User

from random import randint


# Create your views here.

#make five random cards
def makeCard(request, uid, *args, **kwargs):
  idxList = [0,1,2,3,4]
  cardList = []
  user =User.objects.get(user_id=uid)
  users = User.objects.all().exclude(user_id=uid)
  for i in range(5): #make five integers
    card = randint(1, 10)
    while card in cardList: #not for overlapping
      card = randint(1, 10)
    cardList.append(card)
  
  user.cardList = list(zip(idxList,cardList))
  user.save()
  context ={
    "user" : user,
    "users" : users,
  }
  return render(request, "game/attack.html", {"user": user})

# def makeCard(request, uid, *args, **kwargs):
#   idxList = [0,1,2,3,4]
#   cardList = []
#   user =User.objects.get(user_id=uid)
#   users = User.objects.all().exclude(user_id=uid)
#   for i in range(5): #make five integers
#     card = randint(1, 10)
#     while card in cardList: #not for overlapping
#       card = randint(1, 10)
#     cardList.append(card)
  
#   user.cardList = list(zip(idxList,cardList))
#   user.save()
#   context ={
#     "user" : user,
#     "users" : users,
#   }
#   return render(request, "game/counterattack.html", {"user": user})
  
  #make criteria for winning the game
def makeCriteria(request, pk, *args, **kwargs):
  criteriaList = [True, False, 3 , 7]
  idx = randint(0, 3)
  game = Game.objects.get(id = pk)
  hostCard = game.hostUser.card
  guestCard = game.guestUser.card
  
  if idx == 0:
    game.result = hostCard > guestCard
  elif idx == 1:
    game.result = hostCard < guestCard
  #criteria for winning is close to three
  elif idx == 2:
    game.result = abs(hostCard - 3) < abs(guestCard - 3)
  elif idx == 3:
    game.result = abs(hostCard - 7) < abs(guestCard - 7)
    
  game.winner = game.hostUser if game.result else game.guestUser
  
  return render(request, "game/gameStatus.html")

def userCreate(request: HttpRequest, *args, **kwargs):
  print(User.objects.all())
  if request.method == "POST":
    User.objects.create(
      user_id = request.POST["user_id"],
      scoreAll = request.POST["scoreAll"],
      card = request.POST["card"],
    )
    print(User.objects.all())
    return redirect("/")
  return render(request, "game/userCreate.html")


def showstate(request, pk, *args, **kwargs):
    game = Game.objects.get(id = pk)
    hostCard = game.hostUser.card
    guestCard = game.guestUser.card
    if hostCard is not None and guestCard is None: # 게임 진행중..
        ing = True  #list.html 에서 ing를 받아옴
    elif hostCard is None and guestCard is not None: # 반격하기
        ing= False  #list.html 에서 ing을 받아옴
  

    
