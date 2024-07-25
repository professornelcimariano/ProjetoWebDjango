from django.shortcuts import render, get_object_or_404
from core.models import Product, Blog, CategoryProduct
# Create your views here.
# Funções com as Rotas 
# - Função index faz a requisição no arquivo index.html
# - Função contato faz a requisição no arquivo contato.html
def index(request):
    context = {
        'courses': 'Programação de Computadores no SENAC GUA',
        'languages': ['Python', 'Java', 'C#', 'JavaScript'],
        'title': 'Projeto Django',
        'news': [
            {
                'title': 'Nova versão do Django lançada!',
                'subtitle': 'Confira as novidades da versão 3.0',
                'text': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla convallis libero ut imperdiet vehicula.'
            },
            {
                'title': 'Python é a linguagem do futuro',
                'subtitle': 'Especialistas afirmam que Python está dominando o mercado',
                'text': 'Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.'
            }
        ]
    }
    return render(request, 'index.html', context)
    
def contato(request):
    return render(request, 'contato.html', {'title': 'Contato Site'})

def produtos(request):
    product = Product.objects.all() # Products.objects.all() -> Usado para recuperar todos os objetos de um modelo (Dados de uma tabela).
    category = CategoryProduct.objects.all()  # Para exibir todas as categorias no template

    data = {
        'product': product,
        'category': category
    }
    return render(request, 'produtos.html', data)

def produto_single(request, id):
    product = get_object_or_404(Product, id=id) # get_object_or_404(Products, id=id) -> Usado para recuperar um único objeto com base em um critério específico, como um ID único.
    return render(request, 'produto_single.html', {'product': product})  


def blogs(request):
    blog = Blog.objects.all()

    data = {
        'blog': blog,
        'title': 'Blog Django'
    }
    return render(request, 'blogs.html', data)

#Página single do blog com slug, url amigável
def blog_single(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'blog_single.html', {'blog': blog})  

def produtos_categoria(request, cat_name=None):
    product = Product.objects.all()

    if cat_name:
        category = get_object_or_404(CategoryProduct, cat_name=cat_name)
        product = Product.objects.filter(pro_category=category)

    category = CategoryProduct.objects.all()  # Para exibir todas as categorias no template

    return render(request, 'produtos_categoria.html', {'product': product, 'category': category})