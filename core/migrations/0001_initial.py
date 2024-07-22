# Generated by Django 5.0.7 on 2024-07-22 01:39

import core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blo_title', models.CharField(max_length=100, verbose_name='Título')),
                ('blo_subtitle', models.CharField(blank=True, max_length=100, null=True, verbose_name='Sub-Título')),
                ('blo_description', models.TextField(verbose_name='Texto do Blog')),
                ('blo_image', models.ImageField(blank=True, null=True, upload_to='images/blog')),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs',
            },
        ),
        migrations.CreateModel(
            name='CategoryProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=100, unique=True, verbose_name='Nome da Categoria')),
            ],
            options={
                'verbose_name': 'Categoria de Produto',
                'verbose_name_plural': 'Categorias de Produtos',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cli_name', models.CharField(max_length=100)),
                ('cli_cpf', models.CharField(max_length=11, unique=True, validators=[core.validators.validate_cpf])),
                ('cli_email', models.EmailField(max_length=254)),
                ('cli_image', models.ImageField(blank=True, null=True, upload_to='images/cliente')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_name', models.CharField(max_length=100, unique=True, verbose_name='Nome do Produto')),
                ('pro_price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Preço')),
                ('pro_stock', models.IntegerField(blank=True, null=True, verbose_name='Quantidade em Estoque')),
                ('pro_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.categoryproduct')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
            },
        ),
    ]
