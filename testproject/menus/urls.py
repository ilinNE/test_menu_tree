from django.urls import path, re_path
from django.views.generic import TemplateView


urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html"), name="index"),
    path(
        "services/shaving",
        TemplateView.as_view(template_name="index.html"),
        name="shaving",
    ),
    re_path(r"^", TemplateView.as_view(template_name="index.html")),
]
