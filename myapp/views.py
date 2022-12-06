from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render

# Create your views here.


def index(request):
    title = 'Django course!!'
    return render(request, 'index.html', {
        'title': title
    })


def about(request):
    username = 'Marcos'
    return render(request, 'about.html', {
        'username': username
    })


def hello(request, username):
    return HttpResponse(f"<h1>Hello {username}!</h1>")


def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects.html', {
        'projects': projects
    })


def tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {
        'tasks': tasks
    })
