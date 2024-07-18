from django.db import models
#slug
from django.utils.text import slugify
#validação do cpf
from .validators import validate_cpf
# Create your models here.

class Category(models.Model):
    cat_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.cat_name

class Products (models.Model):
    pro_name = models.CharField('Nome', max_length=100, unique=True) # a chave "unique=True" não permitirá cadastrar 2 valores iguais
    pro_price = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    pro_stock = models.IntegerField('Quantidade em Estoque', null=True, blank=True) # null=True Permite campo vazio na tabela e blank=True permite que o registro no input não seja obrigatório
    pro_category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    #A função abaixo é para retornar o name do produto na exibição dentro do painel admin
    def __str__(self):
        return f"{self.pro_name} - {self.pro_category}"
        #return self.pro_name
'''
    def __str__(self):
        return f"{self.name} - R$ {self.price:.2f}"
'''    

class Blogs (models.Model):
    blo_title = models.CharField('Título', max_length=100)
    blo_subtitle = models.CharField('Sub-Título', max_length=100)
    blo_description = models.TextField()
    blo_image = models.ImageField(upload_to='images/', blank=True, null=True)
    # image = models.ImageField(upload_to='images/', default='images/default.jpg')
    slug = models.SlugField(unique=True, blank=True)

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
            while Blogs.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)
    #A função abaixo é para retornar o name do produto na exibição dentro do painel admin
    def __str__(self):
       return self.blo_title

class Cliente(models.Model):
    cli_nome = models.CharField(max_length=100)
    cli_cpf = models.CharField(max_length=11, unique=True, validators=[validate_cpf]) # a chave "unique=True" não permitirá cadastrar 2 valores iguais
    cli_email = models.EmailField()
    cli_foto = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.cli_nome