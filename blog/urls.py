from django.urls import path
from . import views

# http://127.0.0.1:8000/blogs/
# http://127.0.0.1:8000/blogs/my-post-slug/
urlpatterns = [
    path("", views.blog_list, name="blog_list"),
    path("<int:pk>/", views.blog_detail_pk, name="blog_detail_pk"),
    path("<slug:slug>/", views.blog_detail, name="blog_detail"),
]
