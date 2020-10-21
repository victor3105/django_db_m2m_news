from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article, AssignedTags


def articles_list(request):
    template = 'articles/news.html'
    context = {}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'
    articles = Article.objects.order_by(ordering).prefetch_related('scopes')
    a_list = []
    for article in articles:
        tags = AssignedTags.objects.filter(article=article).order_by('-is_main')
        tag_list = []
        for tag in tags:
            tag_list.append({'topic': tag.scope, 'is_main': tag.is_main})
        a_list.append({'title': article.title, 'text': article.text, 'image': article.image,
                       'scopes': tag_list})
    context['object_list'] = a_list
    return render(request, template, context)
