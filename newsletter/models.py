from django.db import models


class Subscriber(models.Model):
    """A newsletter subscriber's email address."""

    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.email
