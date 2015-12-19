from django.http import HttpResponse
from django.views.generic import View, ListView, DetailView

from django.conf import settings

from .models import Inspiration, Contact
from goal.models import Goal

# My first class view, hi everyone!
class GreetingView(View):
    greeting = "Hi, I'm Flavio!"

    def get(self, request):
        return HttpResponse(self.greeting)


# Render the homepage
class HomeView(ListView):
    model = Goal
    template_name = "home.html"
    context_object_name = 'current_goal'

    def get_queryset(self):
        return Goal.objects.current()


# This quotes are the way of life
class InspirationsView(ListView):
    model = Inspiration
    template_name = "inspirations.html"
    context_object_name = 'inspirations'

    def get_queryset(self):
        return Inspiration.objects.filter(bio__active=True)


# How to find me
class ContactsView(ListView):
    model = Contact
    template_name = "contacts.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ContactsView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the contacts
        primary_contacts = Contact.objects.filter(bio__active=True).filter(primary=True)
        secondary_contacts = Contact.objects.filter(bio__active=True).filter(primary=False)
        context = { 
            'primary_contacts': primary_contacts,
            'secondary_contacts': secondary_contacts,
        }
        return context
    
