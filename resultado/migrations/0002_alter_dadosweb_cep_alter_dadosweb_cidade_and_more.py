# Generated by Django 4.2.6 on 2023-10-12 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resultado', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dadosweb',
            name='cep',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='dadosweb',
            name='cidade',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='dadosweb',
            name='datas',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='dadosweb',
            name='descricao',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='dadosweb',
            name='edital',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='dadosweb',
            name='edital_online',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='dadosweb',
            name='endereco',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='dadosweb',
            name='numero_licitacao',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dadosweb',
            name='objeto',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dadosweb',
            name='observacao',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dadosweb',
            name='processo',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='dadosweb',
            name='unidade_licitante',
            field=models.TextField(blank=True, null=True),
        ),
    ]
