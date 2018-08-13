import os
from django.conf import settings
from django.urls import reverse
from django.test import TestCase, override_settings

TEST_BASE_DIR = os.path.join(settings.BASE_DIR, 'components/tests')


class TestComponentListView(TestCase):

    def test_url_resolves(self):
        """"
        URL resolves as expected
        """
        url = reverse('components-list')

        self.assertEqual(url, '/components/')

    @override_settings(BASE_DIR=TEST_BASE_DIR)
    def test_get(self):
        """"
        GET request uses template
        """
        url = reverse('components-list')

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'components/components_list.html')
        self.assertIn('components', response.context)
        components = response.context['components']
        self.assertEqual(len(components), 1)
        self.assertEqual(components[0]['dir'], 'foo')
        self.assertIn('Bar', components[0]['components'])
