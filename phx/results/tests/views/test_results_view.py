from datetime import datetime, timedelta
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from pages.models import Page
from fixtures.models import Fixture
from fixtures.tests.factories import FixtureFactory, CategoryFactory
from ..factories import ResultFactory


class TestResultsView(TestCase):

    def test_url_resolves(self):
        """"
        URL resolves as expected
        """
        url = reverse('results-index')

        self.assertEqual(url, '/results/')

    def test_get(self):
        """"
        GET request uses template
        """
        url = reverse('results-index')
        Page.objects.create(title='results')

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'results/result_list.html')

    def test_result_content(self):
        """"
        GET request retrieves expected result/fixture data in view context
        """
        url = reverse('results-index')
        Page.objects.create(title='results')

        first_fixture = FixtureFactory(title='First Fixture')
        first_result = ResultFactory(fixture=first_fixture)

        response = self.client.get(url)
        self.assertEqual(len(response.context['results']), 1)

        result = response.context['results'].first()
        self.assertEqual(result, first_result)

    def test_result_content_date(self):
        """"
        GET request retrieves expected past result data in view context
        """
        url = reverse('results-index')
        Page.objects.create(title='results')

        # five fixtures in the future, five in the past
        today = datetime.now().date()
        past = today - timedelta(days=7)
        future = today - timedelta(days=-7)
        FixtureFactory.create_batch(5, event_date=past)
        FixtureFactory.create_batch(5, event_date=future)

        # add results for two past fixtures
        past_fixtures = Fixture.objects.filter(
            event_date__lte=timezone.now()
        ).distinct()

        first_past_fixture = past_fixtures.first()
        last_past_fixture = past_fixtures.last()

        first_result = ResultFactory(fixture=first_past_fixture)
        ResultFactory(fixture=last_past_fixture)

        response = self.client.get(url)
        self.assertEqual(len(response.context['results']), 2)

        result = response.context['results'].first()
        self.assertEqual(result, first_result)
        self.assertLessEqual(result.fixture.event_date, today)

    def test_result_search(self):
        """
        GET request retrieves results filtered by search
        """
        Page.objects.create(title='results')
        url = reverse('results-index')

        first_fixture = FixtureFactory(title='First Fixture')
        first_result = ResultFactory(fixture=first_fixture)

        second_fixture = FixtureFactory(title='Second Fixture')
        ResultFactory(fixture=second_fixture)

        response = self.client.get(url, {'search': 'first fixture'})
        self.assertEqual(len(response.context['results']), 1)

        result = response.context['results'].first()
        self.assertEqual(result, first_result)

    def test_result_search_empty(self):
        """
        GET request retrieves results filtered by search (none found)
        """
        Page.objects.create(title='results')
        url = reverse('results-index')

        first_fixture = FixtureFactory(title='First Fixture')
        ResultFactory(fixture=first_fixture)

        second_fixture = FixtureFactory(title='Second Fixture')
        ResultFactory(fixture=second_fixture)

        response = self.client.get(url, {'search': 'third fixture'})
        self.assertEqual(len(response.context['results']), 0)

    def test_result_category_search(self):
        """
        GET request retrieves results filtered by search
        """
        Page.objects.create(title='results')
        url = reverse('results-index')

        first_category = CategoryFactory(title='Cat 1')
        second_category = CategoryFactory(title='Cat 2')

        first_fixture = FixtureFactory(
            title='First Fixture',
            categories=[first_category, second_category]
        )
        first_result = ResultFactory(fixture=first_fixture)

        second_fixture = FixtureFactory(title='Second Fixture')
        ResultFactory(fixture=second_fixture)

        response = self.client.get(url, {'search': 'cat 2'})
        self.assertEqual(len(response.context['results']), 1)

        result = response.context['results'].first()
        self.assertEqual(result, first_result)

    def test_result_category_search_empty(self):
        """
        GET request retrieves results filtered by search
        """
        Page.objects.create(title='results')
        url = reverse('results-index')

        first_category = CategoryFactory(title='Cat 1')
        CategoryFactory(title='Cat 2')

        first_fixture = FixtureFactory(
            title='First Fixture',
            categories=[first_category]
        )
        ResultFactory(fixture=first_fixture)

        second_fixture = FixtureFactory(title='Second Fixture')
        ResultFactory(fixture=second_fixture)

        response = self.client.get(url, {'search': 'cat 3'})
        self.assertEqual(len(response.context['results']), 0)
