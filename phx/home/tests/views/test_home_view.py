from django.test import TestCase

from django.urls import reverse


class TestHomeView(TestCase):

    def test_url_resolves(self):
        """"
        URL resolves as expected
        """
        url = reverse('home-index')

        self.assertEqual(url, '/')

    def test_get(self):
        """"
        GET request uses template
        """
        url = reverse('home-index')

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/home.html')
