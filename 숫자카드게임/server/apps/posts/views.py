from django.shortcuts import render,redirect
from .models import User,GestUser,Game
from django.http.request import HttpRequest
from django.db.models import Q

def login(request:HttpRequest,*args, **kwargs):
    hostUser='1' #호스트 유저 아이디 받아오는곳!
    return(hostUser)

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
    context = {
        "game" : game,
    }
    if game.ing == True:
        return render(request, "posts/game_info_progress.html", context=context )
    elif game.ing == False:
        return render(request, "posts/game_info_result.html", context=context)