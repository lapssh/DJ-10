from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    all_articles = Article.objects.all().prefetch_related('scopes').order_by(ordering)
    for article in all_articles:
        for scope in article.scopes.all():
            attrs = scope.article_by_tag_relation_set.get(article=article)
            scope.is_main = attrs.is_main
            print(scope.is_main)
    context = {
        'object_list': all_articles
    }



    return render(request, template, context)
