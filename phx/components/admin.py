from django.utils.html import format_html
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
    readonly_fields = ['current_image']

    def current_image(self, obj):
        return format_html(
            '<img src="{0}" style="max-width:200px" />'.format(
                obj.image.url
            )
        )

    class Meta:
        abstract = True


class AbstractListItemsAdmin(AbstractComponentAdmin):
    readonly_fields = ['current_image_1', 'current_image_2', 'current_image_3']

    def current_image_1(self, obj):
        return self.current_image(obj.image_1)

    def current_image_2(self, obj):
        return self.current_image(obj.image_2)

    def current_image_3(self, obj):
        return self.current_image(obj.image_3)

    def current_image(self, img):
        return format_html(
            '<img src="{0}" style="max-width:200px" />'.format(
                img.url
            )
        )

    class Meta:
        abstract = True


class AbstractQuoteAdmin(AbstractComponentAdmin):
    readonly_fields = ['current_image']

    def current_image(self, obj):
        return format_html(
            '<img src="{0}" style="max-width:200px" />'.format(
                obj.image.url
            )
        )

    class Meta:
        abstract = True


class AbstractImageAdmin(AbstractComponentAdmin):
    readonly_fields = ['current_image']

    def current_image(self, obj):
        return format_html(
            '<img src="{0}" style="max-width:200px" />'.format(
                obj.image.url
            )
        )

    class Meta:
        abstract = True
