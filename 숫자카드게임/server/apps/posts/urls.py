from django.urls import path
from . import views


app_name='posts' #네임 스페이스


urlpatterns= [
    path("posts/gamelist", views.game_list, name='game_list'),
    path("posts/lanking", views.lanking, name='game_lanking'),

]