from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

class IndexTemplateView(TemplateView):
    template_name = "core/index.html"

