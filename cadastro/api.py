from ninja import NinjaAPI, Schema
from .models import Livro
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict

api = NinjaAPI()

@api.get('livro/')
def listar(request):
    livros = Livro.objects.all() # traz um query set 
    response = [{'id':i.id,'titulo': i.titulo, 'descricao':i.descricao, 'autor':i.autor} for i in livros] # serializa query set
    return response


@api.get('livro/{int:id}')
def listar_livro(request,id: int):
    livro = get_object_or_404(Livro,id=id) 
    livro = model_to_dict(livro) 
    return livro 

@api.get('livro_consulta/')
def listar_consultar(request, id: int = 1 ):
    livro = get_object_or_404(Livro,id=id) 
    livro = model_to_dict(livro) 
    return livro 


class LivroSchema(Schema):
    titulo: str
    descricao: str
    autor: str = None

@api.post('livro', response=LivroSchema)
def livro_criar(request, livro: LivroSchema):
    l1 = livro.dict()
    livro = Livro(**l1)
    livro.save()
    return livro

