from django.urls import path
from ninja import NinjaAPI

api = NinjaAPI()

@api.get("/livro")
def get_livro(request):
    # Replace 'return 1' with the actual logic to retrieve and return livro data
    return 'lsakjdçlfjalsçd'

urlpatterns = [
    path("api/", api.urls),
]
