from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('gallery/', views.gallery, name='gallery'),
    path('blog/', views.blog, name='blog'),
    path('blog/<slug:slug>/', views.blogpage, name='blogpage'),
]