# from django.shortcuts import render
from django.http import HttpResponse

def stores(request):
    return HttpResponse("This is the Country path")