from django.http import HttpResponse

def index(request):
    return HttpResponse("Hey, this is a dope app about some lumpin rocks. This is the index!")
