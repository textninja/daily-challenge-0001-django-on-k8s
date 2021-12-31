import os
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'dtc0001themechange/index.html', {
        "bg_color":  os.getenv("BG_COLOR", None)
    })
