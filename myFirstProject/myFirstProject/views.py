from django.http import HttpResponse
from django.shortcuts import render

# def home_view(request):
#     return render(request, 'homepage.html')
#     # return HttpResponse('<h1>This is Homepage</h1>')

def about_view(request):
    return render(request, 'about.html')
    # return HttpResponse('<h1>This is about page</h1>')