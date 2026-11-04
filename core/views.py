from django.shortcuts import render
from .models import Persona, Project


def home(request):
    return render(request, template_name='core/home.html')


def about(request):
    persona = Persona.objects.first()
    return render(request, template_name='core/about.html', context={'persona': persona})


def contact(request):
    return render(request, template_name='core/contact.html')


def portfolio(request):
    projects = Project.objects.all()
    return render(request, template_name='core/portfolio.html', context={'projects': projects})