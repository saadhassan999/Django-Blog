from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
# Create your views here.

def articles_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/articles_list.html', {'articles':articles})
def articles_detail(request, slug):
    return HttpResponse('This is Slug : ' + slug)
