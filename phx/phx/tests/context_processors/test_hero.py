from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from unittest.mock import Mock
import os

from hero.models import Hero
from pages.models import Page
from ...context_processors.hero import hero


class TestContextProcessorHero(TestCase):

    def setUp(self):
        """
        Mock data, including hero image
        """
        path = os.path.dirname(os.path.abspath(__file__))
        image = SimpleUploadedFile(
            name='hero.jpg',
            content=open(path + '/hero.jpg', 'rb').read(),
            content_type='image/jpeg'
        )
        hero = Hero.objects.create(image=image, caption='test img')
        lorem = Page.objects.create(title='lorem')
        Page.objects.create(title='ipsum', parent=lorem, hero=hero)

    def test_title(self):
        """
        Test that a title is returned for an existing page without a hero
        """
        request = Mock()
        request.path = '/lorem/'

        results = hero(request)
        self.assertEqual(results['hero']['title'], 'lorem')
        self.assertTrue('bg' not in results['hero'])

    def test_hero(self):
        """
        Test that a title is returned for an existing page without a hero
        """
        request = Mock()
        request.path = '/lorem/ipsum/'

        results = hero(request)
        self.assertEqual(results['hero']['title'], 'ipsum')
        self.assertEqual(results['hero']['caption'], 'test img')

    def test_page_not_found(self):
        """
        Test that no content is returned for an non-existent page
        """
        request = Mock()
        request.path = '/lorem/ipsum/dolor/'

        results = hero(request)
        self.assertTrue('title' not in results['hero'])
        self.assertTrue('bg' not in results['hero'])
