
from django.urls import path
from . import views
# http://127.0.0.1:8000/blogs/
# http://127.0.0.1:8000/blogs/5/
urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('<int:pk>/', views.blog_detail, name='blog_detail'),
]
