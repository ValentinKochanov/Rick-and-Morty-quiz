from django.core.exceptions import MultipleObjectsReturned
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404

from .models import Player, Question
from .forms import PlayerForm, CommentForm


def select_player(data):
    """Выбор игрока из БД"""
    try:
        player = Player.objects.get(name=data)
    except MultipleObjectsReturned:
        player = Player.objects.filter(name=data).last()
    return player


def player_create_view(request):
    """Создание игрока"""
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['name']
            form.save()
            player = select_player(data)
            id = 1
            context = {'id': id, 'player': player}
            return render(request, 'main/welcome.html', context)
    form = PlayerForm
    return render(request, 'main/create_player.html', {'form': form})


def game(request, player, id):
    """Выводим вопросы викторины по очереди, считаем правильные ответы"""
    quest = get_object_or_404(Question, id=id)
    player = select_player(player)
    if request.method == 'POST':
        answer = request.POST['answer']
        id += 1
        if answer == quest.try_answer:
            player.result += 1
            player.save()
        if id == 15:
            return HttpResponseRedirect(reverse('result', args=[player]))
        else:
            return HttpResponseRedirect(reverse('game', args=[player, id]))
    else:
        context = {'quest': quest}
        return render(request, 'main/game.html', context)


def result(request, player):
    """Выводим итоги викторины, собираем предложения"""
    player = select_player(player)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=player)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('start'))
        else:
            return render(request, 'main/result.html', {'player': player, 'form': form})
    else:
        form = CommentForm(instance=player)
    return render(request, 'main/result.html', {'player': player, 'form': form})
