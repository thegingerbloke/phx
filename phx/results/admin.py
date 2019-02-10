from django.contrib import admin
from django.db.models import Q
from django.utils import timezone

from fixtures.models import Fixture
from phx.admin import phx_admin

from .models import Result


class ResultAdmin(admin.ModelAdmin):
    # display fixture data on results listing view
    list_display = ['fixture_title', 'fixture_event_date']

    # order list display view by fixture event date
    def get_queryset(self, request):
        qs = super(ResultAdmin, self).get_queryset(request).select_related(
            'fixture').order_by('-fixture__event_date')
        return qs

    def fixture_title(self, obj):
        return obj.fixture.title

    def fixture_event_date(self, obj):
        return obj.fixture.event_date

    # if updating, add custom readonly fixture detail field
    def selected_fixture(self, obj):
        return '{0} ({1})'.format(obj.fixture.title, obj.fixture.event_date)

    # if updating, hide fixture select field
    def get_exclude(self, request, obj):
        return ['fixture', 'author'] if obj else ['author']

    # if adding, hide readonly fixture detail field
    def get_readonly_fields(self, request, obj):
        return [] if obj is None else ['selected_fixture']

    # update dropdown to contain date alongside name
    # fields = ['results_url', 'summary', 'results', 'get_']

    # only list fixtures that don't already have results associated
    # past fixtures from (or created in) the last month only
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "fixture":
            one_month_ago = timezone.now() - timezone.timedelta(days=30)
            kwargs["queryset"] = Fixture.objects.filter(
                Q(fixture__isnull=True) & (
                    (Q(event_date__lte=timezone.now()) & Q(
                        event_date__gte=one_month_ago))
                    | (Q(event_date__lte=timezone.now()) & Q(
                        modified_date__gte=one_month_ago))))

        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()


phx_admin.register(Result, ResultAdmin)
