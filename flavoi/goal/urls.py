from django.conf.urls import patterns, include, url
from .views import AchievementsView

urlpatterns = patterns('',
    url(r'^achievements/$', AchievementsView.as_view(), name='achievements'),
)