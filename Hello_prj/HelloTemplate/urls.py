from django.urls import path
from .views import HelloTemplateView

urlpatterns = [
    path("", HelloTemplateView.as_view(), name="helloTemplate"),
]
