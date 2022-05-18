from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView

from .models import Zone


# class IndexView(TemplateView):
#     template_name = "index.html"


class ZoneListView(ListView):
    model = Zone


class ZoneDetailView(DetailView):
    model = Zone