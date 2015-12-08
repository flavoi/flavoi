from django.conf.urls import url
from .views import AchievementsView, YearArchiveView, MonthArchiveView

urlpatterns = [
    url(r'^achievements/$', AchievementsView.as_view(), name='achievements'),
    url(r'^achievements/([0-9]{4})/$', YearArchiveView.as_view(), name='year_archive'),
    url(r'^achievements/([0-9]{4})/([0-9]{2})/$', MonthArchiveView.as_view(), name='month_archive'),
]