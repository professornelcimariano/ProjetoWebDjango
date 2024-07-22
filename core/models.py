from django.db import models
#slug
from django.utils.text import slugify
#validação do cpf
from .validators import validate_cpf
#format_html pra exibir a imagem em miniatura
from django.utils.html import format_html
# tinymce
from tinymce.models import HTMLField
# Create your models here.
# Documentação Models Python Django - https://docs.djangoproject.com/pt-br/5.0/topics/db/models/

# CamelCase (CategoriaProduto) - Classes em Python (Models e Views)
# snake_case (def calcular_total / def validar_email ) - Variáveis e Funções em Python

class CategoryProduct(models.Model):
    cat_name = models.CharField('Nome da Categoria', max_length=100, unique=True) # a chave "unique=True" não permitirá cadastrar 2 valores iguais

    def __str__(self):
        return self.cat_name

    class Meta:
        verbose_name = "Categoria de Produto"
        verbose_name_plural = "Categorias de Produtos"


#O label 'Nome do Produto' é usado para fornecer um nome amigável para o campo pro_name do modelo em Django, em um Formulário será exibido esse  Label   
#A função __str__(self) é um método especial em Python que define a representação em string de uma instância de um objeto. Quando você imprime um objeto ou converte um objeto para uma string, o método __str__ é chamado para fornecer uma representação legível e útil.
#A classe Meta em um modelo Django é usada para fornecer informações adicionais sobre o modelo - "Verbose Name" Exibe um nome mais legível no singular e "verbose_name_plural" exibe o nome no plural

class Product(models.Model):
    pro_name = models.CharField('Nome do Produto', max_length=100, unique=True) # a chave "unique=True" não permitirá cadastrar 2 valores iguais
    pro_price = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    pro_stock = models.IntegerField('Quantidade em Estoque', null=True, blank=True) # null=True Permite campo vazio na tabela e blank=True permite que o registro no input não seja obrigatório
    pro_category = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, null=True)

    #A função abaixo é para retornar o name do produto na exibição dentro do painel admin
    def __str__(self):
        return f"{self.pro_name} - {self.pro_category}"
        #return self.pro_name    

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"



class Blog(models.Model):
    blo_title = models.CharField('Título', max_length=100)
    blo_subtitle = models.CharField('Sub-Título', max_length=100, blank=True, null=True)
    # blo_description = models.TextField('Texto do Blog')
    blo_description = HTMLField('Texto do Blog')
    blo_image = models.ImageField('Imagem de Capa', upload_to='images/blog', blank=True, null=True)
    # image = models.ImageField(upload_to='images/', default='images/default.jpg')
    slug = models.SlugField(unique=True, blank=True, max_length=255)

    '''
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    '''
    #Abaixo o slug possui a função de adicionar um sufixo caso já exista com o mesmo nome
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.blo_title)
            slug = base_slug
            counter = 1
            while Blog.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)
    
    def mini_image(self):
        if self.blo_image:
            return format_html('<img src="{}" style="height: 100px; width: auto;" />', self.blo_image.url)
        return " "
    mini_image.short_description = 'Imagem de Capa'

    #A função abaixo é para retornar o name do produto na exibição dentro do painel admin
    def __str__(self):
       return self.blo_title

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"


class Client(models.Model):
    cli_name = models.CharField(max_length=100)
    cli_cpf = models.CharField(max_length=11, unique=True, validators=[validate_cpf]) # a chave "unique=True" não permitirá cadastrar 2 valores iguais
    cli_email = models.EmailField()
    cli_image = models.ImageField(upload_to='images/cliente', blank=True, null=True)

    def __str__(self):
        return self.cli_nome

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"