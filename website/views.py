from django.shortcuts import render

# Create your views here.

def homePage(request):
    return render(request, "index.html")

def projectsPage(request):
    return render(request, "projects.html")

def contactPage(request):
    return render(request, "contact.html")

def qualificationsPage(request):
    return render(request, "qualifications.html")