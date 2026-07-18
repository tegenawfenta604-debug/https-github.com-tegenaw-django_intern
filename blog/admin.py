from django.contrib import admin
from . import models


@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "is_published", "number_of_views", "created_at")
    list_filter = ("is_published", "created_at")
    search_fields = ("title", "content")
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ("number_of_views", "created_at", "updated_at")
    fieldsets = (
        (None, {"fields": ("title", "slug", "content")}),
        ("Publishing", {"fields": ("is_published",)}),
        ("Stats", {"fields": ("number_of_views", "created_at", "updated_at")}),
    )