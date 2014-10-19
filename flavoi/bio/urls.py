from django.conf.urls import patterns, include, url
from .views import GreetingView, HomeView, InspirationsView, ContactsView

urlpatterns = patterns('',
    url(r'^hello/$', GreetingView.as_view()),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^inspirations/$', InspirationsView.as_view(), name='inspirations'),
    url(r'^contacts/$', ContactsView.as_view(), name='contacts'),
)