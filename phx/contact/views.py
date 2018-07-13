from django.views import generic
from django.views.generic.edit import FormView
from django.shortcuts import get_object_or_404
from .forms import ContactForm, custom_topics
from pages.models import Page
from pages.views import generate_subnav
from .models import Topic, Message


class ContactIndexView(FormView):
    template_name="contact/contact-index.html"
    form_class = ContactForm
    success_url = '/contact/success'

    def get_context_data(self, **kwargs):
        context = super(ContactIndexView, self).get_context_data(**kwargs)
        context['breadcrumb'] = self.generate_breadcrumb()
        context['page'] = get_object_or_404(Page, slug=self.request.path)
        context['subnav'] = generate_subnav(self.request.path, context['page'])
        return context

    def form_valid(self, form):
        form.send_email()
        self.save_message(form)
        return super().form_valid(form)

    def save_message(self, form):
        # get posted topic id
        # get list of custom topic keys
        # if posted topic id is from custom list, remove before saving
        topic = form.cleaned_data['topic']
        contactless_topics = [
            custom_topic[0] for custom_topic in custom_topics
        ]
        topic = None if topic in contactless_topics else topic

        if topic:
            topic_model = Topic.objects.get(pk=topic)
        else:
            topic_model = None

        message = Message(
            name=form.cleaned_data['name'],
            email=form.cleaned_data['email'],
            topic=topic_model,
            message=form.cleaned_data['message'],
        )
        message.save()

    def generate_breadcrumb(self):
        return [
            {
                'title': 'Home',
                'linkUrl': '/',
            },
            {
                'title': 'Contact',
            }
        ]



class ContactSuccessView(generic.TemplateView):
    template_name="contact/contact-success.html"

    def get_context_data(self, **kwargs):
        context = super(ContactSuccessView, self).get_context_data(**kwargs)
        context['breadcrumb'] = self.generate_breadcrumb()
        context['hero'] = {
            'title': 'Contact'
        }
        return context

    def generate_breadcrumb(self):
        return [
            {
                'title': 'Home',
                'linkUrl': '/',
            },
            {
                'title': 'Contact',
                'linkUrl': '/contact/',
            },
            {
                'title': 'Success',
            }
        ]