from django.views.generic import DetailView, ListView

from .models import Article


class ArticleDetailView(DetailView):
    model = Article
    template_name = "blog/article_detail.html"


class ArticleListView(ListView):
    model = Article
    template_name = "blog/article_list.html"
