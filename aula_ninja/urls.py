# https://www.youtube.com/watch?v=jMDWdh1zhf4&ab_channel=pythonando
from django.contrib import admin
from django.urls import path, include
#from ..cadastro.views import minha_view
from cadastro.views import minha_view
from ninja import NinjaAPI

api = NinjaAPI()


urlpatterns = [
    path('admin/', admin.site.urls),
    path("cadastro/", include('cadastro.urls')),
    path('api/', api.urls),  # Esta linha adiciona as URLs do Django Ninja
    path('', minha_view, name='minha-view'),
]
