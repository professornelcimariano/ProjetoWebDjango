from django.contrib import admin
#Formulários do admin estilizados
from .forms import BlogAdminForm

# Register your models here.
from .models import Product, Blog, Client, CategoryProduct, Status
@admin.register(Status)
class Status(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

admin.site.register(Product)

@admin.register(Blog)
class Blog(admin.ModelAdmin):
    form = BlogAdminForm # Estilização do Form Blog do Admin
    list_display = ['title',  'mini_image' ]
    search_fields = ['title']

@admin.register(Client)
class Client(admin.ModelAdmin):
    list_display = ['name', 'cpf', 'email']
    search_fields = ['name', 'cpf', 'email']

@admin.register(CategoryProduct)
class CategoryProduct(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

