from django.http import HttpResponse


def minha_view(request):
    # Lógica da sua visualização
    resposta_texto = "Bem-vindo à minha página!"
    return HttpResponse(resposta_texto, content_type="text/plain")
