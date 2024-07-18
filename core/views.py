from django.shortcuts import render, get_object_or_404
from core.models import Products, Blogs, Category
# Create your views here.
# Funções com as Rotas 
# - Função index faz a requisição no arquivo index.html
# - Função contato faz a requisição no arquivo contato.html
def index(request):
    context = {
        'courses': 'Programação de Computadores no SENAC GUA',
        'languages': ['Python', 'Java', 'C#', 'JavaScript'],
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
            },
            {
                'title': 'JavaScript: O que esperar do ES10?',
                'subtitle': 'Novas funcionalidades e melhorias na performance',
                'text': 'Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus.'
            }
        ]
    }
    return render(request, 'index.html', context)
    
def contato(request):
    return render(request, 'contato.html')

def produtos(request):
    product = Products.objects.all() # Products.objects.all() -> Usado para recuperar todos os objetos de um modelo (Dados de uma tabela).
    categories = Category.objects.all()  # Para exibir todas as categorias no template

    data = {
        'products': product,
        'categories': categories
    }
    return render(request, 'produtos.html', data)

def produto_single(request, id):
    product = get_object_or_404(Products, id=id) # get_object_or_404(Products, id=id) -> Usado para recuperar um único objeto com base em um critério específico, como um ID único.
    return render(request, 'produto_single.html', {'product': product})  

def blogs(request):
    blog = Blogs.objects.all()

    data = {
        'blogs': blog,
    }
    return render(request, 'blogs.html', data)

#Página single do blog com slug, url amigável
def blog_single(request, slug):
    blog = get_object_or_404(Blogs, slug=slug)
    return render(request, 'blog_single.html', {'blog': blog})  

def produtos_categoria(request, cat_name=None):
    products = Products.objects.all()

    if cat_name:
        category = get_object_or_404(Category, cat_name=cat_name)
        products = products.filter(pro_category=category)

    categories = Category.objects.all()  # Para exibir todas as categorias no template

    return render(request, 'produtos_categoria.html', {'products': products, 'categories': categories})