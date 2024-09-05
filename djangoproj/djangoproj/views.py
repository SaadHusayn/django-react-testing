from django.shortcuts import render 

name = "Saad"

def index(request):
    return render(request, 'index.html', {
        "name":name
    })