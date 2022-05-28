from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(
        request,
        "bio.html",
    )


def tictactoe(request):
    return render(request, "tictactoe.html")


def wordle(request):
    return render(request, "wordle.html")
