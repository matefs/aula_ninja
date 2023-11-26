from django.urls import path
from .api import api

urlpatterns = [
    path('api/', api.urls),  # Note the trailing slash
    # Other URL patterns for your app
]
