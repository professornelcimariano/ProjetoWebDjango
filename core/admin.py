from django.contrib import admin
#Formulários do admin estilizados
from .forms import BlogAdminForm

# Register your models here.
from .models import Product, Blog, Client, CategoryProduct

admin.site.register(Product)

#admin.site.register(Blog)
@admin.register(Blog)
class Blog(admin.ModelAdmin):
    form = BlogAdminForm # Estilização do Form Blog do Admin
    list_display = ['mini_image', 'blo_title']
    search_fields = ['blo_title']

@admin.register(Client)
class Client(admin.ModelAdmin):
    list_display = ['cli_name', 'cli_cpf', 'cli_email']
    search_fields = ['cli_name', 'cli_cpf', 'cli_email']

#admin.site.register(CategoryProduct)
@admin.register(CategoryProduct)
class CategoryProduct(admin.ModelAdmin):
    list_display = ['cat_name']
    search_fields = ['cat_name']