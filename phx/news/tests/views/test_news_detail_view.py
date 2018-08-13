from factory import SubFactory
from django.test import TestCase
from django.urls import reverse

from ..factories import (
    NewsFactory,
    ComponentFactory,
    EditorialFactory,
    FeatureFactory,
    QuoteFactory,
    ImageFactory,
    ListItemsFactory,
)


class TestNewsDetailsView(TestCase):

    def test_url_resolves(self):
        """"
        URL resolves as expected
        """
        news = NewsFactory(title='this? is& a! (test*)')
        url = reverse(
            'news-detail', kwargs={'pk': news.id, 'slug': news.slug}
        )

        self.assertEqual(url, '/news/1/this-is-a-test')

    def test_get(self):
        """"
        GET request uses template
        """
        news = NewsFactory(title='this? is& a! (test*)')
        url = reverse(
            'news-detail', kwargs={'pk': news.id, 'slug': news.slug}
        )

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'news/news_detail.html')

    def test_get_no_article(self):
        """"
        GET request returns a 404 when no article found
        """
        url = reverse(
            'news-detail', kwargs={'pk': 9999, 'slug': 'this is a test'}
        )

        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, 'error/error.html')

    def test_previous_next(self):
        """"
        GET request returns previous and next articles
        """
        news_1 = NewsFactory(title='article 1')
        news_2 = NewsFactory(title='article 2')
        news_3 = NewsFactory(title='article 3')
        url = reverse(
            'news-detail', kwargs={'pk': news_2.id, 'slug': news_2.slug}
        )

        response = self.client.get(url)
        self.assertEqual(response.context['news'], news_2)
        self.assertEqual(
            response.context['data']['previous']['link_url'],
            '/news/{}/{}'.format(news_1.id, news_1.slug)
        )
        self.assertEqual(
            response.context['data']['next']['link_url'],
            '/news/{}/{}'.format(news_3.id, news_3.slug)
        )

    def test_component_editorial(self):
        """"
        GET request returns editorial component as expected
        """
        news = NewsFactory()
        editorial = EditorialFactory(
            title='first editorial block',
            component=SubFactory(ComponentFactory, news=news))

        url = reverse(
            'news-detail', kwargs={'pk': news.id, 'slug': news.slug}
        )

        response = self.client.get(url)
        component = response.context['components'].first()
        first_editorial = component.editorial
        self.assertEqual(first_editorial, editorial)
        self.assertEqual(first_editorial.title, 'first editorial block')

    def test_component_feature(self):
        """"
        GET request returns feature component as expected
        """
        news = NewsFactory()
        feature = FeatureFactory(
            title='first feature block',
            component=SubFactory(ComponentFactory, news=news))

        url = reverse(
            'news-detail', kwargs={'pk': news.id, 'slug': news.slug}
        )

        response = self.client.get(url)
        component = response.context['components'].first()
        first_feature = component.feature
        self.assertEqual(first_feature, feature)
        self.assertEqual(first_feature.title, 'first feature block')

    def test_component_quote(self):
        """"
        GET request returns quote component as expected
        """
        news = NewsFactory()
        quote = QuoteFactory(
            quote='first quote block',
            component=SubFactory(ComponentFactory, news=news))

        url = reverse(
            'news-detail', kwargs={'pk': news.id, 'slug': news.slug}
        )

        response = self.client.get(url)
        component = response.context['components'].first()
        first_quote = component.quote
        self.assertEqual(first_quote, quote)
        self.assertEqual(first_quote.quote, 'first quote block')

    def test_component_image(self):
        """"
        GET request returns image component as expected
        """
        news = NewsFactory()
        image = ImageFactory(
            caption='first image block',
            component=SubFactory(ComponentFactory, news=news))

        url = reverse(
            'news-detail', kwargs={'pk': news.id, 'slug': news.slug}
        )

        response = self.client.get(url)
        component = response.context['components'].first()
        first_image = component.image
        self.assertEqual(first_image, image)
        self.assertEqual(first_image.caption, 'first image block')

    def test_component_list_items(self):
        """"
        GET request returns list_items component as expected
        """
        news = NewsFactory()
        list_items = ListItemsFactory(
            title_1='first list_items block',
            component=SubFactory(ComponentFactory, news=news))

        url = reverse(
            'news-detail', kwargs={'pk': news.id, 'slug': news.slug}
        )

        response = self.client.get(url)
        component = response.context['components'].first()
        first_list_items = component.list_items
        self.assertEqual(first_list_items, list_items)
        self.assertEqual(first_list_items.title_1, 'first list_items block')
