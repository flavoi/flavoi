from django.conf.urls import url
from .views import AchievementsView, YearArchiveView

urlpatterns = [
    url(r'^achievements/$', AchievementsView.as_view(), name='achievements'),
    url(r'^achievements/([0-9]{4})/$', YearArchiveView.as_view(), name='year_archive'),
]