from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View

from django.conf import settings

from .models import Inspiration, Contact
from goal.models import Goal

# My first class view, hi everyone!
class GreetingView(View):
    greeting = "Hi, I'm Flavio!"

    def get(self, request):
        return HttpResponse(self.greeting)

# Render the homepage
class HomeView(View):
    template_name = "home.html"
    current_goal = Goal.objects.latest('modified')
    context = {
        'current_goal': current_goal,
    }
    def get(self, request):
        return render(request, self.template_name, self.context)

# This quotes are the way of life
class InspirationsView(HomeView):
    template_name = "inspirations.html"
    inspirations = Inspiration.objects.filter(bio__active=True)
    context = { 'inspirations': inspirations }

# How to find me
class ContactsView(HomeView):
    template_name = "contacts.html"
    contacts = Contact.objects.filter(bio__active=True)
    context = { 'contacts': contacts }
