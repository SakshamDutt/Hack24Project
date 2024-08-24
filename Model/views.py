from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def homeView(request) -> HttpResponse:
    return HttpResponse("On Home View")