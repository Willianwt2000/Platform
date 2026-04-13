from django.http import HttpResponse

def customers(request):
    return HttpResponse("This is a customers paths")   # http://127.0.0.1:8000/users/customers

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)   #http://127.0.0.1:8000/users/5/


def results(request, question_id):
    response = "You're looking at the results of question %s."  #http://127.0.0.1:8000/users/5/results/
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)   #http://127.0.0.1:8000/users/5/vote/
