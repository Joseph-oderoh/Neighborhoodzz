from . import views
from django.urls import path, re_path
urlpatterns = [
    path('', views.homepage, name='landing'),
    path('hoodz/', views.hoods, name='hood'),
    path('new_hoodz/', views.create_hood, name='new-hood'),
]