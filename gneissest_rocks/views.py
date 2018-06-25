from django.shortcuts import render

def index(request):
    return HttpResponse("Hey, this is a dope app about some lumpin rocks. This is the index!")
