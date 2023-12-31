from django.http import HttpResponse
from django.shortcuts import render
from .models import Article

# Create your views here.
def article_list(req):
    articles = Article.objects.all().order_by('date')
    return render(req, 'articles/article_list.html', { 'articles': articles})

def article_detail(req, slug):
    article = Article.objects.get(slug=slug)
    print('-article', article, '-all', Article.objects.all())
    return HttpResponse(article)
