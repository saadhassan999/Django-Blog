from django.db import models
from django.conf import settings

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)

    # article class method to return string
    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + " ..."