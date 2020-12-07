from django.shortcuts import render, redirect
from .models import Article
from .forms import CreateArticle
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
    if request.method == "POST":
        form = CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save() 
            return redirect('articles:list')
    else:
        form = CreateArticle()
    return render(request, 'articles/create_articles.html', {'form' : form})