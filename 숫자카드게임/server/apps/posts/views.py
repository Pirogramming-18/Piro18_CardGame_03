from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from .forms import UserForm
from .models import User,GestUser,Game
from django.http.request import HttpRequest
from django.db.models import Q

from random import randint

def login(request:HttpRequest,*args, **kwargs):
    hostUser='1' #호스트 유저 아이디 받아오는곳!
    return(hostUser)
    
def main(request, *args, **kwargs):
    return render(request, "main.html")

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserForm()
    return render(request, 'posts/signup.html', {'form':form})

def game_list(request:HttpRequest,*args, **kwargs): #hostUser 받아와야함.
    hostname='1'
    game_list=Game.objects.all()
    if game_list:
        user_game=Game.objects.filter(Q(hostUser=hostname)| Q(guestUser=hostname))
    else:
        print("신규 유저")
    context={
        'hostname':hostname,
        'user_game':user_game
        }        
    return render(request,"posts/game_list.html",context=context)

def lanking(request:HttpRequest,*args, **kwargs):
    userlanking=User.objects.order_by('-scoreAll')
    context={
        'userlanking':userlanking,
        }       
    return render(request,"posts/game_lanking.html",context=context)

def game_info(request, pk, *args, **kwargs) :
    game = Game.objects.get(pk=pk)
    user='1'
    context = {
        "game" : game,
        "user":user,
    }
    return render(request, "posts/game_info.html", context=context )


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