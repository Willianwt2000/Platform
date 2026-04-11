from django.http import HttpResponse

def customers(request):
    return HttpResponse("This is a customers paths")