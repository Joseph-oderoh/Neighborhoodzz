from . import views
from django.urls import path, re_path
urlpatterns = [
    path('', views.homepage, name='landing'),
    path('all-hoods/', views.hoods, name='hood'),
]