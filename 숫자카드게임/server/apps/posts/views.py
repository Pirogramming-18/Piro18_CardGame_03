from django.shortcuts import render, redirect
from server.apps.posts.models import User, GuestUser, Game


def game_info(request, pk, *args, **kwargs) :
    game = Game.objects.get(pk=pk)
    context = {
        "game" : game,
    }
    return render(request, "games/game_info.html", context=context )
