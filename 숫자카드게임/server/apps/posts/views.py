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
  print(users)
  print(user)
  for i in range(5): #make five integers
    card = randint(1, 10)
    while card in cardList: #not for overlapping
      card = randint(1, 10)
    cardList.append(card)
  print(cardList)
  
  user.cardList = list(zip(idxList,cardList))
  user.save()
  print(user.cardList)
  context ={
    "user" : user,
    "users" : users,
  }
  
  return render(request, "game/attack.html", context=context)

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

# def cardCreate(request: HttpRequest, uid, *args, **kwargs):
#   user =User.objects.get(user_id=uid)
#   if request.method == "POST":
#     user.card = request.POST["card"]
#     user.save()
#     return redirect(f"/attack/{user.user_id}")
#   return render(request, "attack.html")