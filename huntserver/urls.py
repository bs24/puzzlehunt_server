"""puzzlehunt_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from . import views

urlpatterns = [
    # ex: /
    url(r'^$', views.index, name='index'),
    # ex: /puzzles/53f/
    url(r'^(?P<puzzle_id>[0-9a-fA-F]{3})/$', views.puzzle, name='puzzle'),
    # ex: /hunt/3/
    url(r'^(?P<hunt_num>[0-9]+)/$', views.hunt, name='hunt'),
    # ex: /stats/
    url(r'^stats/$', views.public_stats, name='public_stats'),
]