from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    tag = models.ManyToManyField('Scope', through='AssignedTags', null=True, blank=True)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Scope(models.Model):
    topic = models.CharField(max_length=100, verbose_name='Раздел')
    main = models.BooleanField()

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    def __str__(self):
        main_str = 'main' if self.main else 'secondary'
        return f'{self.name}, {main_str}'


class AssignedTags(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    scope = models.ForeignKey(Scope, on_delete=models.CASCADE)

    def __str__(self):
        return f'Article {self.article}: {self.scope}'

    class Meta:
        verbose_name = 'Связанный раздел'
        verbose_name_plural = 'Связанные разделы'
