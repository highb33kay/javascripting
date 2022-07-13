from django.shortcuts import render

# Create your views here.

def score(request):
    return render(request, "scores/scores.html")