from django.urls import path
from games.views import home
from games.views import GameListView
urlpatterns = [
    path("", GameListView.as_view(), name='home'),
]

