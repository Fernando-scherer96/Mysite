# Importa a classe HttpResponse do módulo django.http.
# HttpResponse é usada para enviar respostas HTTP do servidor para o cliente.

# Importa a classe genérica View de django.views.
# A classe genérica View fornece uma maneira de definir views baseadas em classes.
from django.views import generic

from blog.models import Post

# Define a classe PostView, que herda de generic.View.
# Isso permite que você crie uma view personalizada com métodos para lidar
# com diferentes tipos de requisições HTTP (como GET, POST, etc.).
class PostView(generic.ListView):
    queryset = Post.objects.filter(status = 1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
