from django.shortcuts import render
import re

def index(request):
    return render(request, "regex_app/index.html")

def confirm(request):
    return render(request)