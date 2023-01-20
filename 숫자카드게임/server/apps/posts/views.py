from django.shortcuts import render,redirect
from .models import User,GestUser,Game
from django.http.request import HttpRequest
from django.db.models import Q

def login(request:HttpRequest,*args, **kwargs):
    hostUser='1' #호스트 유저 아이디 받아오는곳!
    return(hostUser)
    
def game_list(request:HttpRequest,*args, **kwargs): #hostUser 받아와야함.
    game_list=Game.objects.all()
    hostname='1'
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