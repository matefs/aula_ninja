from django.urls import path
from .api import api
#from .views import minha_view

urlpatterns = [
    path('api/', api.urls),  # Note the trailing slash
    # Other URL patterns for your app
    # path('', minha_view, name='minha-view'),

]
