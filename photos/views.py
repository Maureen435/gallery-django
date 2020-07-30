from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.db.models import Q
from .models import Images

def home(request):
    images = Images.objects.all()
    return render(request, "home.html", {"images":images})

