from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('bio.urls', namespace='bio')),
    url(r'^blog/', include('goal.urls', namespace='blog')),
]
