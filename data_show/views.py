from django.http import Http404
from django.shortcuts import render

from . import models


# Create your views here.
def index(request):
    club_names = models.Club.objects.all()
    context = {
        'club_names': club_names
    }
    return render(request, 'data_show/index.html', context)


def club_detail(request, club_name):
    try:
        club = models.Club.objects.get(name=club_name)
        context = {
            'club': club,
        }
    except models.Club.DoesNotExist:
        raise Http404("Club does not exist")
    return render(request, 'data_show/club_detail.html', context)


def test(request):
    try:
        context = {
            'student': models.Student.objects.get(id=1),
        }
    except models.Contact.DoesNotExist:
        raise Http404('Contact does not exist')
    return render(request, 'data_show/test.html', context)
