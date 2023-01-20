from django.urls import path
from django.contrib.auth import views as auth_views
from server.apps.posts.views import main
from . import views

app_name='posts' #네임 스페이스
urlpatterns= [
    path("", main),
    path('login/', auth_views.LoginView.as_view(template_name='posts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path("posts/gamelist", views.game_list, name='game_list'),
    path("posts/lanking", views.lanking, name='game_lanking'),
    path('posts/gameinfo/<int:pk>', views.game_info, name='game_info')
]