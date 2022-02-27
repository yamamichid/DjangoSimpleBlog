from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import DetailView, ListView, CreateView, TemplateView

from .forms import CommentForm
from .models import Article, Comment


class HomeView(TemplateView):
    template_name = "blog/home.html"
    extra_context = {
        'title': 'Home',
    }

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        response.context_data['articles'] = Article.objects.order_by('-created_at').all()
        return response


class ArticleDetailView(DetailView):
    model = Article
    template_name = "blog/article_detail.html"

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        response.context_data['comment_form'] = CommentForm()
        return response

    def post(self, request, *args, **kwargs):
        if "like" in request.POST:
            article = Article.objects.get(pk=self.kwargs["pk"])
            article.like += 1
            article.save()
        return redirect(reverse("blog:article-detail", kwargs={"pk": self.kwargs["pk"]}))


class ArticleListView(ListView):
    model = Article
    template_name = "blog/article_list.html"


class CommentCreateView(CreateView):
    http_method_names = ["post"]
    model = Comment
    fields = ["author", "text"]

    def form_valid(self, form):
        form.instance.article_id = self.kwargs["article_id"]
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("blog:article-detail", kwargs={"pk": self.kwargs["article_id"]})
