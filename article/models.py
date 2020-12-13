from django.db import models


class Article(models.Model):
    title = models.CharField('Название статьи', max_length=150)
    content = models.TextField('Текст статьи', )
    created_at = models.DateTimeField('Дата публикации', auto_now_add=True)
    updated_at = models.DateTimeField('Дата последней редакции', auto_now=True)
    is_published = models.BooleanField(default=True)
    like = models.BooleanField('Лайк', default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at']


def img_directory_path(instance, filename):
    return '{0}/{1}'.format(instance.article.title, filename)


class Image(models.Model):
    title = models.CharField('Название Изображения', blank=True, max_length=150)
    upload = models.ImageField('Загрузить в', upload_to=img_directory_path)
    article = models.ForeignKey('Article', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
