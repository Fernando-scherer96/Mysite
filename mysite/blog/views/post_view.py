# Importa a classe HttpResponse do módulo django.http.
# HttpResponse é usada para enviar respostas HTTP do servidor para o cliente.
from django.http import HttpResponse

# Importa a classe genérica View de django.views.
# A classe genérica View fornece uma maneira de definir views baseadas em classes.
from django.views import generic

# Define a classe PostView, que herda de generic.View.
# Isso permite que você crie uma view personalizada com métodos para lidar
# com diferentes tipos de requisições HTTP (como GET, POST, etc.).
class PostView(generic.View):

    # Define o método get, que é chamado quando uma requisição HTTP GET é recebida.
    # 'self' refere-se à instância da classe PostView.
    # 'request' é o objeto HttpRequest recebido, contendo informações sobre a requisição HTTP.
    # '*args' e '**kwargs' são argumentos e argumentos de palavra-chave variáveis que podem ser passados,
    # mas não são usados neste método específico.
    def get(self, request, *args, **kwargs):
        # Retorna um objeto HttpResponse contendo o texto 'Hello World'.
        # Isso será exibido ao cliente que fez a requisição GET.
        return HttpResponse('Hello World')