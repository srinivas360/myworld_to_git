from django.http import HttpResponse
from django.shortcuts import render
from .models import Article
from django.contrib.auth.decorators import login_required

# Create your views here.
def article_list(req):
    articles = Article.objects.all().order_by('date')
    return render(req, 'articles/article_list.html', { 'articles': articles})

def article_detail(req, slug):
    article = Article.objects.get(slug=slug)
    print('--detail view fun -article', article)
    return render(req, 'articles/article_detail.html', {'article': article})

@login_required(login_url=None)
def article_create(request):
    return render(request, 'articles/article_create.html')