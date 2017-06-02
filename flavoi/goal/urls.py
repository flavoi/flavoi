from django.conf.urls import url
from .views import AchievementsView, AchievementsThemeListView, AchievementsDetailView, AchievementsSearchView

urlpatterns = [
    url(r'^$', AchievementsView.as_view(), name='achievements'),
    url(r'^theme/(?P<theme>[-\w]+)/$', AchievementsThemeListView.as_view(), name='achievements_theme'),
    url(r'^(?P<slug>[-\w]+)/(?P<pk>[-\w]+)/$', AchievementsDetailView.as_view(), name='achievement_detail'),
    url(r'^search/$', AchievementsSearchView.as_view(), name='achievement_search'),
]