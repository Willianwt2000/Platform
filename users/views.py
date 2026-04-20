from django.http import HttpResponse
from django.shortcuts import render
from .models import Customer

def customers(request):
    customer = Customer.objects.filter(id__gt=200 )
    context = {"customer": customer}
    return render(request,"users/users.html",context)   # http://127.0.0.1:8000/users/customers

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)   #http://127.0.0.1:8000/users/5/


def results(request, question_id):
    response = "You're looking at the results of question %s."  #http://127.0.0.1:8000/users/5/results/
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)   #http://127.0.0.1:8000/users/5/vote/
