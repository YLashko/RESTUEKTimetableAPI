from django.http import HttpResponse
from django.shortcuts import render
from .scraper.timetable_utils import get_table_json
from .database_utils import save_json_table, get_table
from .interface import get_by_date, get_by_date_start_time
import json


def main(request):
    return HttpResponse("Hello")


def scraper_test(request):
    a = get_by_date_start_time("184251", "2022-12-05", "18:30")
    context = {"test_content": a}
    return render(request, "static/test.html", context)
