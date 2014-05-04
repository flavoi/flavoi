from django.shortcuts import render

from bio.views import HomeView
from .models import Goal


# My job goals reside here
class AchievementsView(HomeView):
    template_name = "achievements.html"
    current_goal = Goal.objects.filter(published=True)