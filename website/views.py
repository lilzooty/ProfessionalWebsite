from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def homePage(request):
    return render(request, "index.html")

def projectsPage(request):
    return render(request, "projects.html")

def contactPage(request):
    return render(request, "contact.html")

def skillsPage(request):
    return render(request, "skills.html")

def ping(request):
    return JsonResponse({'message': 'pong'})