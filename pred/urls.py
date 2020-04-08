from django.conf.urls import url
from django.contrib import admin
from .views import (searchposts)
from .views import (post)

urlpatterns = [
     url(r'^$', searchposts, name='searchposts'),
     url(r'form', post, name='post'),
]