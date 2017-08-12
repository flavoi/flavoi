from django.http import HttpResponse
from django.views.generic import View, ListView, DetailView

from django.conf import settings

from .models import Inspiration, Contact, Momenti
from goal.models import Goal


# My first class view, hi everyone!
class GreetingView(View):
    greeting = "Hi, I'm Flavio!"

    def get(self, request):
        return HttpResponse(self.greeting)


# Render the homepage
class HomeView(ListView):
    model = Goal
    template_name = "about.html"
    context_object_name = 'current_goal'

    def get_queryset(self):
        return Goal.objects.current()

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        reports = []
        inspirations = ('inspirations', Inspiration.objects.all().count())
        reports.append(inspirations)
        momenti = ('momenti', Momenti.objects.all().count())
        reports.append(momenti)
        goals = ('ideas', Goal.objects.history().count())
        reports.append(goals)
        context['reports'] = reports
        return context


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


# This is me, and the most important people of my life
class MomentiView(ListView):
    model = Momenti
    context_object_name = 'momenti'

    def get_queryset(self):
        return Momenti.objects.filter(bio__active=True)
