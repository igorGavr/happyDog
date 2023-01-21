from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class IndexPage(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "Li"
        return context