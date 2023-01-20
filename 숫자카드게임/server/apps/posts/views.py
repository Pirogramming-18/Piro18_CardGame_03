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
  # print(users)
  # print(user)
  for i in range(5): #make five integers
    card = randint(1, 10)
    while card in cardList: #not for overlapping
      card = randint(1, 10)
    cardList.append(card)
  # print(cardList)
  
  user.cardList = list(zip(idxList,cardList))
  user.save()
  # print(user.cardList)
  context ={
    "user" : user,
    "users" : users,
  }
  
  return render(request, "game/attack.html", context=context)

#make five random cards
def makeCard2(request, uid, *args, **kwargs):
  idxList = [0,1,2,3,4]
  cardList = []
  user =User.objects.get(user_id=uid)
  users = User.objects.all().exclude(user_id=uid)
  # print(users)
  # print(user)
  for i in range(5): #make five integers
    card = randint(1, 10)
    while card in cardList: #not for overlapping
      card = randint(1, 10)
    cardList.append(card)
  # print(cardList)
  
  user.cardList = list(zip(idxList,cardList))
  user.save()
  # print(user.cardList)
  context ={
    "user" : user,
    "users" : users,
  }
  
  return render(request, "game/counterattack.html", context=context)

#make criteria for winning the game
def gameStart(request, pk, *args, **kwargs):
  # criteriaList = [True, False, 3 , 7]
  criteriaList = [True, False]
  idx = randint(0, 1)
  game = Game.objects.get(id = pk)
  hostUser = game.hostUser
  guestUser = game.guestUser
  hostCard = game.hostUser.card
  guestCard = game.guestUser.card
  rule = "큰" if criteriaList[idx] else "작은"
  context = {
    "hostUser" : hostUser,
    "guestUser" : guestUser,
    "game" : game,
    "rule" : rule,
  }
  
  
  if idx == 0:
    game.result = "승리" if hostCard > guestCard else "패배"
  elif idx == 1:
    game.result = "승리" if hostCard < guestCard else "패배"
  #criteria for winning is close to three
  # elif idx == 2:
  #   game.result = "승리" if abs(hostCard - 3) < abs(guestCard - 3) else "패배"
  # elif idx == 3:
  #   game.result = "승리" if abs(hostCard - 7) < abs(guestCard - 7) else "패배"
    
  game.winner = game.hostUser if game.result =="승리" else game.guestUser
  
  if game.result == "승리":
    game.hostUser.scoreAll += game.hostUser.card
    game.guestUser.scoreAll -= game.hostUser.card
  else:
    game.hostUser.scoreAll -= game.hostUser.card
    game.hostUser.scoreAll += game.hostUser.card
  
  return render(request, "game/gameStatus.html", context=context)

    
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

def scoreUpdate(request: HttpRequest, pk, *args, **kwargs):
  game = Game.objects.get(id=pk)
  
  if game.result == "승리":
    game.hostUser.scoreAll += game.hostUser.card
    game.guestUser.scoreAll -= game.hostUser.card
  else:
    game.hostUser.scoreAll -= game.hostUser.card
    game.hostUser.scoreAll += game.hostUser.card
  return redirect("/")

#수정 필요
def GameCreate(request: HttpRequest, uid, *args, **kwargs):
  
  idxList = [0,1,2,3,4]
  cardList = []
  user =User.objects.get(user_id=uid)
  users = User.objects.all().exclude(user_id=uid)
  # print(users)
  # print(user)
  for i in range(5): #make five integers
    card = randint(1, 10)
    while card in cardList: #not for overlapping
      card = randint(1, 10)
    cardList.append(card)
  # print(cardList)
  
  user.cardList = list(zip(idxList,cardList))
  user.save()
  # print(user.cardList)
  context ={
    "user" : user,
    "users" : users,
  }

  if request.method == "POST":
    # user.card = request.POST["card"]
    # user.save()
    Game.objects.create(
      hostUser = user,
      guestUser = User.objects.get(user_id =  request.POST.get("guestUser")),
      result = "시작전",
      winner = "",
      ing = False,
      standard = False,
      score = 0,
      accept = False,
    )
    game = Game.objects.get(hostUser=user, guestUser=User.objects.get(user_id =  request.POST.get("guestUser")))
    print(game.guestUser.user_id)
    return redirect(f"/counterattack/{game.id}",  context=context)

  return render(request, "game/attack.html", context=context)



def counterattack(request: HttpRequest, pk, *args, **kwargs):
  
  idxList = [0,1,2,3,4]
  cardList = []
  game = Game.objects.get(id=pk)
  hostUser = game.hostUser
  user = game.guestUser
  print(game.guestUser.user_id)
  for i in range(5): #make five integers
    card = randint(1, 10)
    while card in cardList: #not for overlapping
      card = randint(1, 10)
    cardList.append(card)
  # print(cardList)
  
  user.cardList = list(zip(idxList,cardList))
  user.save()
  print(user.card)
  # print(user.cardList)
  context ={
    "game" : game,
    "user" : user,
  }

  if request.method == "POST":
    print("hello")
    game.accept=True
    game.save()
    return redirect(f"/counterattack/{game.id}",  context=context)
    # return redirect(f"gameStatus/{game.id}",  context=context)

  return render(request, "game/counterattack.html", context=context)



def showstate(request, pk, *args, **kwargs):
    game = Game.objects.get(id = pk)
    hostCard = game.hostUser.card
    guestCard = game.guestUser.card
    if hostCard is not None and guestCard is None: # 게임 진행중..
        ing = True  #list.html 에서 ing를 받아옴
    elif hostCard is None and guestCard is not None: # 반격하기
        ing= False  #list.html 에서 ing을 받아옴