from django.db import models
from django.utils.text import slugify


class Blog(models.Model):
    """A single blog post."""

    title = models.CharField(max_length=200)
    slug = models.SlugField(
        max_length=220,
        unique=True,
        blank=True,
        help_text="URL-friendly identifier. Auto-generated from the title if left blank.",
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(
        default=False,
        verbose_name="published",
        help_text="Only published posts are visible to site visitors.",
    )
    number_of_views = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "blog post"
        verbose_name_plural = "blog posts"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
