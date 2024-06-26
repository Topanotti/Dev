# Generated by Django 5.0.3 on 2024-03-21 12:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fornecedor', '0001_initial'),
        ('requisicao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_comprarequisicao', models.BooleanField(default=False, verbose_name='Associação com Requisição')),
                ('is_compraitem', models.BooleanField(default=False, verbose_name='Associação com Itens')),
                ('data', models.DateField()),
                ('descricao', models.CharField(max_length=200)),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fornecedor.fornecedor')),
                ('requisicao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='requisicao.requisicao')),
            ],
        ),
    ]
