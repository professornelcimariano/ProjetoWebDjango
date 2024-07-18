from django.contrib import admin


# Register your models here.

from .models import Products, Blogs, Cliente, Category

admin.site.register(Products)
admin.site.register(Blogs)

@admin.register(Cliente)
class Cliente(admin.ModelAdmin):
    list_display = ['cli_nome', 'cli_cpf', 'cli_email']
    search_fields = ['cli_nome', 'cli_cpf', 'cli_email']

admin.site.register(Category)