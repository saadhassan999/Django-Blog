from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

def articles_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/articles_list.html', {'articles':articles})

def articles_detail(request, slug):
    # return HttpResponse('This is Slug : ' + slug)
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/articles_detail.html', {'article' : article})

@login_required(login_url='/accounts/login')
def create_article(request):
    return render(request, 'articles/create_articles.html')