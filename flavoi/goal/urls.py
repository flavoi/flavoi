from django.conf.urls import patterns, include, url
from .views import AchievementsView, YearArchiveView

urlpatterns = patterns('',
    url(r'^achievements/$', AchievementsView.as_view(), name='achievements'),
    url(r'^achievements/([0-9]{4})/$', YearArchiveView.as_view(), name='year_archive'),
)