from django.db import models
from markdownx.models import MarkdownxField


class Article(models.Model):
    title = models.CharField(max_length=200)
    text = MarkdownxField('Content', help_text='Write your content here.', default='')
    image = models.ImageField(upload_to='images/', default='images/default-headline-image.jpg')
    like = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.created_at.date()}-{self.title}'


class Comment(models.Model):
    author = models.CharField(max_length=200)
    text = MarkdownxField('Content', help_text='Write your content here.', default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author}-{self.created_at.date()}-{self.article.title}'


class BlogConfig(models.Model):
    ID = 1
    title = models.CharField(max_length=200, default='Title')
    description = models.TextField(default='')
    favicon = models.ImageField(upload_to='favicon', default='favicon/favicon.ico')

    def save(self, *args, **kwargs):
        self.pk = self.ID
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=cls.ID)
        return obj

    def __str__(self):
        return 'BlogConfig'
