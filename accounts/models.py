from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """Extra user information living alongside the built-in User model."""

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField(blank=True, help_text="Short biography shown on the author profile.")
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
    website = models.URLField(blank=True)
    # Timestamps for "recent activity" style displays.
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} profile"
