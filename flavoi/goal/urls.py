from django.conf.urls import url
from .views import AchievementsView, AchievementsThemeListView, AchievementsDetailView, AchievementsSearchView

urlpatterns = [
    url(r'^$', AchievementsView.as_view(), name='home'),
    url(r'^theme/(?P<theme>[-\w]+)/$', AchievementsThemeListView.as_view(), name='theme'),
    url(r'^search/$', AchievementsSearchView.as_view(), name='search'),
    url(r'^(?P<slug>[-\w]+)/$', AchievementsDetailView.as_view(), name='detail'),
]