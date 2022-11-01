from django.contrib import admin
from django.urls import include, path
from .views import main, scraper_test

urlpatterns = [
    path("", main, name="main"),
    path("test/", scraper_test, name="scraper_test")
]
