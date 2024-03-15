# Importando classes necessárias do Django
from django.db import models
from django.contrib.auth.models import User

# STATUS é uma lista de tuplas definindo possíveis estados para um post.
# Cada tupla contém um valor inteiro e sua descrição correspondente.
STATUS = [
    (0, 'Draft'),   # 'Draft' indica que o post está em rascunho.
    (1, 'Publish')  # 'Publish' indica que o post está publicado.
]

# Definição da classe Post, que herda de models.Model, 
# indicando que Post é um modelo do Django.
class Post(models.Model): 
    # Campo para o título do post.
    # max_length=200 define o comprimento máximo do texto.
    # unique=True garante que cada título seja único.
    title = models.CharField(max_length=200, unique=True)

    # Campo para o slug (versão amigável da URL) do post.
    # Tem as mesmas propriedades que o título.
    slug = models.SlugField(max_length=200, unique=True)

    # Campo que estabelece uma relação muitos-para-um com o modelo User.
    # Isso significa que um usuário pode ser autor de vários posts.
    # on_delete=models.CASCADE especifica que, se o usuário for excluído, 
    # seus posts também serão.
    # related_name="blog_posts" permite acessar os posts de um usuário.
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")

    # Campo de data/hora que é automaticamente atualizado para a data/hora atual
    # sempre que o objeto Post é salvo.
    update_on = models.DateTimeField(auto_now=True)

    # Campo para o conteúdo do post, permitindo texto longo sem limite de comprimento.
    content = models.TextField()

    # Campo de data/hora que registra quando o post foi criado.
    # auto_now_add=True faz com que a data/hora seja definida para o momento
    # em que o post é criado.
    created_on = models.DateTimeField(auto_now_add=True)

    # Campo para o status do post, utilizando as opções definidas em STATUS.
    # default=0 define que o estado padrão é 'Draft'.
    status = models.IntegerField(choices=STATUS, default=0)

    # Metaclasse que define opções adicionais para o modelo Post.
    # ordering = ['-created_on'] define a ordenação padrão dos posts
    # por data de criação em ordem decrescente.
    class Meta: 
        ordering = ['-created_on']

    # Método mágico __str__ que define como um objeto Post é representado como string.
    # Neste caso, retorna o título do post.
    def __str__(self):
        return self.title
