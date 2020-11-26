from django.shortcuts import render
from django.views.generic.base import TemplateView
from services.models import Service

# Create your views here.

class IndexTemplateView(TemplateView):
    template_name = "core/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = Service.objects.all()
        return context
    

