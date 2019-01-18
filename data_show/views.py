from django.http import Http404
from django.shortcuts import render

from . import models


# Create your views here.
def index(request):
    club_names = models.Club.objects.extra(order_by=['name'])
    context = {
        'club_names': club_names
    }
    return render(request, 'data_show/clubs_list.html', context)


def club_card(request, club_name):
    try:
        club = models.Club.objects.get(name=club_name)
        context = {
            'club': club,
        }
    except models.Club.DoesNotExist:
        raise Http404("Club does not exist")
    return render(request, 'data_show/club_card.html', context)
