from django.shortcuts import render

from utils import decorators
from utils import functions

from .models import Game

import json


def index(request):
    return render(request, 'app/index.html', {'logged_in' : functions.logged_in(request)})


@decorators.logged_in(required_permission=2)
def create_object(request):

    Game.objects.create(
        title="An awesome murder mystery",
        description="A very long and interesting description about the murder mystery",
        time=160,
        languages=['english', 'dutch'],
        player_amounts=[8, 10],
        age=18,
        themes=['Violence', 'Alcohol', 'Relationships'],
        tested=True
    )

    return render(request, 'app/create_object.html')