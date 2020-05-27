from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from pred import views

urlpatterns = [
    url('', include(('pred.urls', 'pred'), namespace='search')),
    url('admin/', admin.site.urls),
]
