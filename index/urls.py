from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^$', Index_Views),
    url(r'^login/$', Index_Views, name='login'),
    url('^register/$', Register_Views, name='register'),
    url(r'^quit/$', Quit_Views, name='quit'),
    url(r'^management/', include('management.urls'), name='management'),
]
