from django.shortcuts import render
from django.views.generic import TemplateView


class Navbar(TemplateView):
    template_name = 'navbar.html'


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')
