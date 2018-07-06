import nested_admin


class AbstractComponentsAdmin(nested_admin.NestedStackedInline):
    extra = 0
    max_num = 1

    class Meta:
        abstract = True


class AbstractEditorialsAdmin(AbstractComponentsAdmin):
    class Meta:
        abstract = True


class AbstractFeaturesAdmin(AbstractComponentsAdmin):
    class Meta:
        abstract = True


class AbstractListItemsAdmin(AbstractComponentsAdmin):
    class Meta:
        abstract = True


class AbstractQuotesAdmin(AbstractComponentsAdmin):
    class Meta:
        abstract = True


class AbstractImagesAdmin(AbstractComponentsAdmin):
    class Meta:
        abstract = True
