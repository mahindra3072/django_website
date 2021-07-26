from django.shortcuts import render
from .models import Movies
from django import forms
import re

class NewSearch(forms.Form):
   
   title= forms.CharField(label="Movie Name")


def imdb(request):

        if request.method == 'POST':
                form= NewSearch(request.POST)
                if form.is_valid():
                    search = form.cleaned_data["title"].strip()
                    searchcap =capitalizeWords(search)
                    y=Movies.objects.filter(title=search)
                    x=Movies.objects.filter(title=searchcap)
                    
                    context={
        
        'rawtxt':y,       
        'info':x
        
                    }
                    return render(request,"imdbratings/imdbpage.html",context)
                else:
                    return render(request,"imdbratings/imdbpage.html",{
                        'form':form
                        })


        

    
        return render(request,"imdbratings/imdbpage.html",{'form':NewSearch()})


def capitalizeWords(s):
  return re.sub(r'\w+', lambda m:m.group(0).capitalize(), s)
