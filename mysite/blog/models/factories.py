# Importando as bibliotecas necessárias
import factory
from faker import Factory as FakerFactory

# Importando modelos do Django
from django.contrib.auth.models import User
from django.utils.timezone import now

# Corrigindo a importação do modelo Post (deve começar com letra maiúscula)
from blog.models import Post

# Criando uma instância do Faker para gerar dados fictícios
faker = FakerFactory.create()

# Definição da factory para o modelo User do Django
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        # Especifica o modelo Django que a factory irá utilizar
        model = User

    # Gerando email fictício
    email = factory.Faker('safe_email')
    # Gerando nome de usuário fictício
    username = factory.LazyAttribute(lambda x: faker.name())

    @classmethod
    def _prepare(cls, create, **kwargs):
        # Extraíndo senha, se fornecida, dos kwargs
        password = kwargs.pop('password', None)
        # Chamando método _prepare da classe pai para criar o objeto User
        user = super(UserFactory, cls)._prepare(create, **kwargs)

        # Se uma senha foi fornecida, defina-a para o usuário
        if password:
            user.set_password(password)
            # Se estivermos criando (e não apenas construindo), salve o usuário
            if create:
                user.save()
        return user
    
# Definição da factory para o modelo Post
class PostFactory(factory.django.DjangoModelFactory):
    # Especificando o modelo Django
    class Meta:
        model = Post

    # Gerando título fictício para o post
    title = factory.LazyAttribute(lambda x: faker.sentence())
    # Definindo data e hora de criação como o momento atual
    created_on = factory.LazyAttribute(lambda x: now())
    # Associando um autor ao post, usando a UserFactory
    author = factory.SubFactory(UserFactory)
    # Definindo status inicial do post
    status = 0
