# Generated by Django 3.1.4 on 2020-12-23 22:04

import article.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='description',
            field=models.TextField(default='dsfd', verbose_name='Описание'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=article.models.Article.upload_path, verbose_name='Обложка статьи'),
        ),
    ]
