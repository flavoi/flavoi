from django.conf.urls import url
from .views import AchievementsView, AchievementsThemeListView, AchievementsDetailView, AchievementsSearchView

urlpatterns = [
    url(r'^achievements/$', AchievementsView.as_view(), name='achievements'),
    url(r'^achievements/theme/(?P<theme>[-\w]+)/$', AchievementsThemeListView.as_view(), name='achievements_theme'),
    url(r'^achievements/(?P<pk>[-\w]+)/$', AchievementsDetailView.as_view(), name='achievement_detail'),
    url(r'^achievements/search/results/$', AchievementsSearchView.as_view(), name='achievement_search'),
]