from django.http import HttpResponse

def index(request):
    return HttpResponse("Hey, this is a dope app about some lumpin rocks. This is the index!")

def detail(request, rock_id):
    return HttpResponse("You're looking at rock %s." & rock_id)

def results(request, rock_id):
    response = "You're looking at the results of rock %s."
    return HttpResponse(response % question_id)
