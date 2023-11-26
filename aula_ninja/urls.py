# https://www.youtube.com/watch?v=jMDWdh1zhf4&ab_channel=pythonando
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/',admin.site.urls),
    path("cadastro/",include('cadastro.urls'))
]
