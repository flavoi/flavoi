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


# My gob goals of a set year
class YearArchiveView(AchievementsView):
    
    def get_queryset(self):
        year = self.args[0]
        return Goal.objects.current_year(year)
