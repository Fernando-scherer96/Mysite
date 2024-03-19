from django.contrib import admin

# Register your models here.

from .models import Post

class PostAdmin(admin.ModelAdmin): 
    #vai exibir uma lista com todos os posts criados
    list_display =('title', 'slug', 'created_on')
    #vai mostrar um label para nos ver o que quermos filtrar
    list_filter = ('status',)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)