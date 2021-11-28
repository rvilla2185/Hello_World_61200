from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HelloTemplateView(TemplateView):
    template_name = "helloTemplate.html"
