from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return HttpResponse("Hello you can contact me on yashchoudhary4477")
