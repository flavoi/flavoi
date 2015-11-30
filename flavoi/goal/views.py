from django.shortcuts import render
from django.views.generic import ListView

from .models import Goal


# My job goals reside here
class AchievementsView(ListView):
    model = Goal
    template_name = "achievements.html"
    context_object_name = 'published_goals'
    
    def get_queryset(self):
        return Goal.objects.history()