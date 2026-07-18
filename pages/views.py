from django.views.generic import TemplateView


class HomePageView(TemplateView):
    """Landing page. Uses the global base template for a consistent layout."""

    template_name = "pages/home.html"


class AboutPageView(TemplateView):
    """Static About page describing the project."""

    template_name = "pages/about.html"


class ContactPageView(TemplateView):
    """Static Contact page (renders the contact form template)."""

    template_name = "pages/contact.html"
