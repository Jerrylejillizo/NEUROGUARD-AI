from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('analyze-password/', views.analyze_password, name='analyze_password'),
    # If you want analyze-url, you must add it:
    path('analyze-url/', views.analyze_url, name='analyze_url'),
]