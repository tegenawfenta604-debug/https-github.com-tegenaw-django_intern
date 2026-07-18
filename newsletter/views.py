from django.shortcuts import redirect
from django.views.decorators.http import require_POST


@require_POST
def subscribe(request):
    """Newsletter subscription handler (full implementation in a later step)."""
    # Placeholder: real logic (model + email) added with the Newsletter feature.
    return redirect("home")
