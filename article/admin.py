from django.contrib import admin
from .models import Article, Image


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    exclude = ('like',)
    list_display = ('title', 'created_at', 'updated_at', 'is_published')


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'article')
    list_display_links = ('title', 'article')
