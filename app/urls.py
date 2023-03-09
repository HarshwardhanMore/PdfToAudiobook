from django.contrib import admin
from django.urls import path, include
from app import urls
from . import views


from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index),
    path('index', views.index),
    path('player', views.player),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
