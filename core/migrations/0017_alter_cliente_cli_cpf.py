# Generated by Django 5.0.6 on 2024-07-18 21:36

import core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_alter_cliente_cli_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cli_cpf',
            field=models.CharField(max_length=11, unique=True, validators=[core.validators.validate_cpf]),
        ),
    ]
