from django.http import HttpResponse
from django.shortcuts import render
from .interface import get_by_date, get_by_date_start_time
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


def main(request):
    return HttpResponse("Hello")


def scraper_test(request, group_id, date):
    a = get_by_date(group_id, date)
    context = {"test_content": a}
    return render(request, "static/test.html", context)


@api_view(["GET"])
def get_date(request):
    try:
        data = get_by_date(request.GET.get("group_id"), request.GET.get("date"))
    except:
        return Response({"message": "Please specify parameters group_id, date correctly"},
                        status=status.HTTP_400_BAD_REQUEST)
    return Response(data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_datetime(request):
    try:
        data = get_by_date_start_time(request.GET.get("group_id"), request.GET.get("date"), request.GET.get("time"))
    except:
        return Response({"message": "Please specify parameters group_id, date, time correctly"},
                        status=status.HTTP_400_BAD_REQUEST)
    return Response(data, status=status.HTTP_200_OK)
