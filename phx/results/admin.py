from django.utils import timezone
from django.contrib import admin
from .models import Results
from fixtures.models import Fixtures


class ResultsAdmin(admin.ModelAdmin):
    # display fixture data on results listing view
    list_display = ['fixture_title', 'fixture_event_date']

    # order list display view by fixture event date
    def get_queryset(self, request):
        qs = super(ResultsAdmin, self).get_queryset(request).select_related('fixture').order_by('-fixture__event_date')
        return qs

    def fixture_title(self, obj):
        return obj.fixture.title

    def fixture_event_date(self, obj):
        return obj.fixture.event_date

    # if updating, add custom readonly fixture detail field
    def selected_fixture(self, obj):
        return '{0} ({1})'.format(
            obj.fixture.title,
            obj.fixture.event_date
        )

    # if updating, hide fixture select field
    def get_exclude(self, request, obj):
        return ['fixture'] if obj else []

    # if adding, hide readonly fixture detail field
    def get_readonly_fields(self, request, obj):
        return [] if obj is None else ['selected_fixture']

    # update dropdown to contain date alongside name
    # fields = ['results_url', 'summary', 'results', 'get_']

    # only list past fixtures that don't already have results associated
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "fixture":
            kwargs["queryset"] = Fixtures.objects.filter(
                fixture__isnull=True,
                event_date__lte=timezone.now(),
            )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Results, ResultsAdmin)
