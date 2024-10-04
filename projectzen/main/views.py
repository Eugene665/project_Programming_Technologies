from django.shortcuts import render
from .models import Project

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def all_projects(request):
    projects = Project.objects.all()
    return render(request, 'main/all_projects.html', {'title': 'Проекты на платформе', 'projects': projects})
