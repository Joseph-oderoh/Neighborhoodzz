from . import views
from django.urls import path, re_path
urlpatterns = [
    path('', views.homepage, name='landing'),
    path('hoodz/', views.hoods, name='hood'),
    path('new_hoodz/', views.create_hood, name='new-hood'),
    path('profile/<username>', views.profile, name='profile'),
    path('profile/<username>/edit/', views.edit_profile, name='edit-profile'),
    path('join_hood/<id>', views.join_hood, name='join-hood'),
    path('leave_hood/<id>', views.leave_hood, name='leave-hood'),
]