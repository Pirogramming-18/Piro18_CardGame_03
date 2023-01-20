from django.shortcuts import render
# from server.apps.posts.models import User, GestUser, Game

def main(request, *args, **kwargs):
    return render(request, "main.html")
