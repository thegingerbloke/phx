from django.test import TestCase
from django.urls import reverse

from ..factories import NewsFactory


class TestNewsListView(TestCase):
    def test_url_resolves(self):
        """"
        URL resolves as expected
        """
        url = reverse('news-list')

        self.assertEqual(url, '/news/')

    def test_get(self):
        """"
        GET request uses template
        """
        url = reverse('news-list')

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'news/news_list.html')

    def test_get_search(self):
        """"
        GET request uses search string, tested against news title/summary
        """
        NewsFactory(title='The big w race')
        NewsFactory(summary='The blackcap race')
        NewsFactory.create_batch(8)

        url = reverse('news-list')
        response = self.client.get(url)
        self.assertEqual(len(response.context['news']), 10)

        response = self.client.get(url, {'search': 'big w race'})
        self.assertEqual(len(response.context['news']), 1)

        response = self.client.get(url, {'search': 'blackcap'})
        self.assertEqual(len(response.context['news']), 1)

    def test_get_search_empty(self):
        """"
        GET request uses search string, no results
        """
        NewsFactory.create_batch(10)

        url = reverse('news-list')
        response = self.client.get(url)
        self.assertEqual(len(response.context['news']), 10)

        response = self.client.get(url, {'search': 'Bleurgh'})
        self.assertEqual(len(response.context['news']), 0)
