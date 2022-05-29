from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,DetailView
from django.shortcuts import render

from games.models import Game
class GameListView(ListView):
    model=Game
    template_name='games/home.html'
    context_object_name='game_list'
class GameDetailView( LoginRequiredMixin , DetailView ):
    model=Game
    content_object_name="game"
def home(request):
    return render(request, 'home.html')


