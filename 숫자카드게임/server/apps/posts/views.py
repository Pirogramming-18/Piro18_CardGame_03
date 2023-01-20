from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from .forms import UserForm
from .models import User,GestUser,Game
from django.http.request import HttpRequest
from django.db.models import Q

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
