from django.urls import path
from . import views

app_name = 'games'
urlpatterns = [
    path('gameinfo/<int:pk>', views.game_info, name='game_info')
]