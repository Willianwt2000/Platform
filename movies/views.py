from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Actor



def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)   #http://127.0.0.1:8000/movies/5/


def results(request, question_id):
    response = "You're looking at the results of question %s."  #http://127.0.0.1:8000/movies/5/results/
    return HttpResponse(response % question_id)


# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)   #http://127.0.0.1:8000/movies/5/vote/


def vote(request, film_id):
    return HttpResponse("Estás votando por la película con ID %s." % film_id)

# Actor
def actor(request):
    latest_actors_list = Actor.objects.order_by("-last_update")[:10]
    # output = ", ".join([f"{q.first_name} {q.last_name}" for q in latest_actors_list])

    template = loader.get_template("movies/index.html")
    context = {"latest_actors_list": latest_actors_list}
    # return HttpResponse(output)
    # return HttpResponse(template.render(context, request))

    # shortcut render()
    return render(request, "movies/index.html",context)

def movies(request):
    return HttpResponse("This is a Movie paths")