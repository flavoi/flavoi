from datetime import date
import operator

from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import Goal


# My job goals reside here
class AchievementsView(ListView):
    model = Goal
    template_name = "achievements.html"
    context_object_name = 'published_goals'
    paginate_by = 5

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


# Get the whole content of a single goal 
class AchievementsDetailView(DetailView):
    model = Goal
    template_name = "achievements_details.html"
    context_object_name = 'published_goal_detail'


# Display an Achievement List page filtered by the search query.
class AchievementsSearchView(AchievementsView):

    def get_queryset(self):
        result = super(AchievementsView, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            print query_list
            result = result.filter(
                reduce(operator.and_,
                       (Q(title__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(abstract__icontains=q) for q in query_list))
            )
        return result
