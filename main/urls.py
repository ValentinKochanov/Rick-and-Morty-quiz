from django.urls import path
from .views import game, result, player_create_view


urlpatterns = [
    path('', player_create_view, name='start'),
    path('game/<str:player>/<int:id>/', game, name='game'),
    path('result/<str:player>/', result, name='result'),
]
