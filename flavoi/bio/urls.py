from django.conf.urls import url
from .views import GreetingView, HomeView, InspirationsView, ContactsView, MomentiView

urlpatterns = [
    # url(r'^hello/$', GreetingView.as_view()),
    url(r'^$', HomeView.as_view(), name='about'),
    # url(r'^inspirations/$', InspirationsView.as_view(), name='inspirations'),
    # url(r'^contacts/$', ContactsView.as_view(), name='contacts'),
    # url(r'^momenti/$', MomentiView.as_view(), name='momenti'),
]