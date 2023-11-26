from ninja import NinjaAPI
from .models import Livro

api = NinjaAPI()

@api.get('livro/')
def listar(request):
    livros = Livro.objects.all()
    response = [{'id':i.id,'titulo': i.titulo, 'descricao':i.descricao, 'autor':i.autor} for i in livros]
    return response


