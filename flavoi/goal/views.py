from django.shortcuts import render

from bio.views import HomeView
from .models import Goal


# My job goals reside here
class AchievementsView(HomeView):
    template_name = "achievements.html"
    published_goals = Goal.objects.filter(published=True).order_by('modified')
    context = {
        'published_goals': published_goals,
    }
    def get(self, request):
        return render(request, self.template_name, self.context)
