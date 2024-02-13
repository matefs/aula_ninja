from django.http import HttpResponse


def minha_view(request):
    # Lógica da sua visualização
    resposta_texto = "Tente acessar /api/docs"
    return HttpResponse(resposta_texto, content_type="text/plain")
