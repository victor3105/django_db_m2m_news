from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    context = {}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'
    articles = Article.objects.order_by(ordering).prefetch_related('tag')
    articles_l = []
    for article in articles:
        tags = []
        for tag in article.tag.all():
            tags.append(tag)
        articles_l.append({'title': article.title, 'text': article.text, 'image': article.image, 'scopes': tags})

    # articles_list()
    context['object_list'] = articles_l

    return render(request, template, context)
