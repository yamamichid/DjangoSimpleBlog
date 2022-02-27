from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('articles', views.ArticleListView.as_view(), name='article-list'),
    path('article/<int:pk>', views.ArticleDetailView.as_view(), name='article-detail'),
    path('article/<int:article_id>/comment', views.CommentCreateView.as_view(), name='comment-create'),
]
