from django.shortcuts import render, redirect
from server.apps.posts.models import User, GuestUser, Game


def game_info(request, pk, *args, **kwargs) :
    game = Game.objects.get(pk=pk)
    context = {
        "game" : game,
    }
    if game.ing == True:
        return render(request, "games/game_info_progress.html", context=context )
    elif game.ing == False:
        return render(request, "games/game_info_result.html", context=context)
