from django.test import TestCase
from django.urls import reverse

from blog.models import Article


class ArticleDetailViewTestCase(TestCase):

    def test_article_detail_view_success_status_code(self):
        article = Article.objects.create(
            title='Test Article',
            text='This is a test article'
        )
        url = reverse('blog:article-detail', args=(article.id,))

        response = self.client.get(url)

        self.assertEquals(response.status_code, 200)


class ArticleListViewTestCase(TestCase):

    def test_article_list_view_success_status_code(self):
        url = reverse('blog:article-list')

        response = self.client.get(url)

        self.assertEquals(response.status_code, 200)
