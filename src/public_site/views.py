from django.http import HttpResponse


def index(request):
    return HttpResponse("Ezen az oldalon a Dél-Hevesben zajló természetvédelmi munkákról tájékozódhat.")
