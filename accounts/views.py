from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.views.generic import TemplateView
from .forms import RegistrationForm, ProfileForm
from .models import Profile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Auto-create a Profile whenever a new User is created."""
    if created:
        Profile.objects.create(user=instance)


def register(request):
    """Handle user registration; log the user in on success."""
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")
    else:
        form = RegistrationForm()
    return render(request, "accounts/register.html", {"form": form})


def user_logout(request):
    """Log the current user out and redirect home."""
    logout(request)
    return redirect("home")


class DashboardView(TemplateView):
    """Authenticated user landing page (requires login)."""

    template_name = "accounts/dashboard.html"

    def dispatch(self, request, *args, **kwargs):
        # Re-use Django's login_required behaviour without a decorator.
        if not request.user.is_authenticated:
            return redirect("login")
        return super().dispatch(request, *args, **kwargs)


@login_required
def profile_update(request):
    """Let the logged-in user edit their Profile."""
    profile = request.user.profile
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form = ProfileForm(instance=profile)
    return render(request, "accounts/profile_update.html", {"form": form})


def author_profile(request, username):
    """Public profile page for a given author."""
    user = get_object_or_404(User, username=username)
    return render(request, "accounts/author_profile.html", {"author": user})
