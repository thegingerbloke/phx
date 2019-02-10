from django.test import TestCase
from django.urls import reverse

from ..factories import GalleryFactory


class TestGalleryListView(TestCase):
    def test_url_resolves(self):
        """"
        URL resolves as expected
        """
        url = reverse('gallery-list')

        self.assertEqual(url, '/gallery/')

    def test_get(self):
        """"
        GET request uses template
        """
        url = reverse('gallery-list')

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gallery/gallery_list.html')

    def test_get_search(self):
        """"
        GET request uses search string, tested against gallery title/summary
        """
        GalleryFactory(title='The big w race')
        GalleryFactory(summary='The blackcap race')
        GalleryFactory.create_batch(8)

        url = reverse('gallery-list')
        response = self.client.get(url)
        self.assertEqual(len(response.context['gallery_list']), 10)

        response = self.client.get(url, {'search': 'big w race'})
        self.assertEqual(len(response.context['gallery_list']), 1)

        response = self.client.get(url, {'search': 'blackcap'})
        self.assertEqual(len(response.context['gallery_list']), 1)

    def test_get_search_empty(self):
        """"
        GET request uses search string, no results
        """
        GalleryFactory.create_batch(10)

        url = reverse('gallery-list')
        response = self.client.get(url)
        self.assertEqual(len(response.context['gallery_list']), 10)

        response = self.client.get(url, {'search': 'Bleurgh'})
        self.assertEqual(len(response.context['gallery_list']), 0)
