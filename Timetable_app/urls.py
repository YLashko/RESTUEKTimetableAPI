from django.contrib import admin
from django.urls import include, path
from .views import main, scraper_test, get_date, get_datetime

urlpatterns = [
    path("", main, name="main"),
    path("test/<str:group_id>/<str:date>", scraper_test, name="scraper_test"),
    path("date", get_date),
    path("datetime", get_datetime)
]
