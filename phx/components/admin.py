import nested_admin


class AbstractComponentAdmin(nested_admin.NestedStackedInline):
    extra = 0
    max_num = 1

    class Meta:
        abstract = True


class AbstractEditorialAdmin(AbstractComponentAdmin):
    class Meta:
        abstract = True


class AbstractFeatureAdmin(AbstractComponentAdmin):
    class Meta:
        abstract = True


class AbstractListItemsAdmin(AbstractComponentAdmin):
    class Meta:
        abstract = True


class AbstractQuoteAdmin(AbstractComponentAdmin):
    class Meta:
        abstract = True


class AbstractImageAdmin(AbstractComponentAdmin):
    class Meta:
        abstract = True
