from django.urls import path
from .views import show, home_view

urlpatterns = [
    path('', show),
    path('form/', home_view)
]