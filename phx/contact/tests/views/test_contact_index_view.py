from django.test import TestCase, override_settings
from django.urls import reverse

from pages.models import Page
from ...models import Message, Topic
from ...forms import ContactForm


class TestContactIndexView(TestCase):

    def test_url_resolves(self):
        """"
        URL resolves as expected
        """
        url = reverse('contact-index')

        self.assertEqual(url, '/contact/')

    def test_get(self):
        """"
        GET request uses template
        """
        url = reverse('contact-index')
        Page.objects.create(title='contact')

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact-index.html')
        self.assertIsInstance(response.context['form'], ContactForm)

    @override_settings(CONTACT_EMAIL='test@test.com')
    def test_post(self):
        """
        Valid POST saves Message model instance
        """
        url = reverse('contact-index')
        Page.objects.create(title='contact')

        response = self.client.post(
            url,
            {
                'name': 'Lorem Ipsum',
                'email': 'lorem@ipsum.com',
                'topic': 'misc',
                'message': 'This is a test'
            },
            follow=True
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Message.objects.count(), 1)

        message = Message.objects.first()
        self.assertEqual(message.name, 'Lorem Ipsum')
        self.assertEqual(message.email, 'lorem@ipsum.com')
        self.assertEqual(message.message, 'This is a test')

    @override_settings(CONTACT_EMAIL='test@test.com')
    def test_post_custom_topic(self):
        """
        Valid POST saves Message model instance with custom topic
        """
        url = reverse('contact-index')
        Page.objects.create(title='contact')
        Topic.objects.create(topic='Test topic')

        response = self.client.post(
            url,
            {
                'name': 'Lorem Ipsum',
                'email': 'lorem@ipsum.com',
                'topic': '1',
                'message': 'This is a test'
            },
            follow=True
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Message.objects.count(), 1)

        message = Message.objects.first()
        self.assertEqual(message.name, 'Lorem Ipsum')
        self.assertEqual(message.topic, Topic.objects.first())

    def test_post_invalid(self):
        """
        Invalid POST returns form with errors, no Message model saved
        """
        url = reverse('contact-index')
        Page.objects.create(title='contact')

        response = self.client.post(
            url,
            {
                'name': 'Lorem Ipsum',
                'email': 'lorem@ipsum.com',
                # 'topic': 'missing topic',
                'message': 'This is a test'
            },
            follow=True
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['form'].errors, {
            'topic': ['This field is required.'],
        })
        self.assertEqual(Message.objects.count(), 0)
