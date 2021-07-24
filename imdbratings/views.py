from django.shortcuts import render

# Create your views here.

def imdb(request):
    
    return render(request,'imdbratings/imdbpage.html')
