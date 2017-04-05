from datetime import date
import operator

from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import Goal, GoalTheme


# My goals in all history
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
        # Add in a timestamp for the goal
        context['themes'] = GoalTheme.objects.all()
        context['history_link_class'] = 'current'
        return context


# My goals of a set theme
class AchievementsThemeListView(AchievementsView):
    def get_queryset(self):
        theme = self.kwargs['theme']
        return Goal.objects.get_goals_by_theme(theme)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(AchievementsThemeListView, self).get_context_data(**kwargs)
        context['this_link_class'] = self.kwargs['theme']
        context['history_link_class'] = 'link'
        return context


# Get the whole content of a single goal 
class AchievementsDetailView(DetailView):
    model = Goal
    context_object_name = 'published_goal_detail'


# Display an Achievement List page filtered by the search query.
class AchievementsSearchView(AchievementsView):

    def get_queryset(self):
        result = super(AchievementsView, self).get_queryset()
        result = result.get_all_active_goals() # active goals only, even if the query is empty
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

    def get_context_data(self, **kwargs):
        context = super(AchievementsSearchView, self).get_context_data(**kwargs)
        context['history_link_class'] = 'link'
        context['year_link_class'] = 'link'
        context['month_link_class'] = 'link'
        context['search_query'] = self.request.GET.get('q')
        return context