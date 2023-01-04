from django.urls import path, re_path
from django.views.generic import TemplateView


urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html"), name="index"),
    path(
        "services/shaving",
        TemplateView.as_view(template_name="index.html"),
        name="shaving",
    ),
    path(
        "services/haircut",
        TemplateView.as_view(template_name="index.html"),
        name="haircut",
    ),
    path(
        "services/drying",
        TemplateView.as_view(template_name="index.html"),
        name="drying",
    ),
    path(
        "services/nails/manicure",
        TemplateView.as_view(template_name="index.html"),
        name="manicure",
    ),
    path(
        "services/nails/nail_extension",
        TemplateView.as_view(template_name="index.html"),
        name="nail",
    ),
    re_path(r"^", TemplateView.as_view(template_name="index.html")),
]
