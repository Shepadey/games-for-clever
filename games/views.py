from django.views.generic import ListView
from django.shortcuts import render

from games.models import Game
class GameListView(ListView):
    model=Game
    template_name='games/home.html'
    context_object_name='game_list'
def home(request):
    return render(request, 'home.html')


