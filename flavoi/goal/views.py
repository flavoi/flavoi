from datetime import date

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

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(AchievementsView, self).get_context_data(**kwargs)
        # Add in a timestamp for the archive
        context['current_year'] = date.today().year
        context['current_month'] = date.today().month
        return context


# My goals in a set year
class YearArchiveView(AchievementsView):
    
    def get_queryset(self):
        year = self.args[0]
        return Goal.objects.get_year_archive(year)


# My goals in a set month
class MonthArchiveView(AchievementsView):
    
    def get_queryset(self):
        year = self.args[0]
        month = self.args[1]
        return Goal.objects.get_month_archive(year, month)