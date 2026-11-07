from django.urls import path, include
from . import views

urlpatterns = [
    path('api/', include('social_app.urls')),
    path("", views.home, name="home"),
    path("health/", views.health_check, name="health"),
]


