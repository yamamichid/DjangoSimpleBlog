from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from .models import Article, Comment, BlogConfig


admin.site.register(Comment)
admin.site.register(Article, MarkdownxModelAdmin)
admin.site.register(BlogConfig)
