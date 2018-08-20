from easy_thumbnails.files import get_thumbnailer
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


class AbstractEmbedAdmin(AbstractComponentAdmin):
    class Meta:
        abstract = True


class AbstractFeatureAdmin(AbstractComponentAdmin):
    readonly_fields = ['current_image']

    def current_image(self, obj):
        thumbnailer = get_thumbnailer(obj.image)
        thumbnail_options = {'size': (200, 200)}
        return format_html(
            '<img src="/media/{0}" />'.format(
                thumbnailer.get_thumbnail(thumbnail_options)
            )
        )

    class Meta:
        abstract = True


class AbstractImageAdmin(AbstractComponentAdmin):
    readonly_fields = ['current_image']

    def current_image(self, obj):
        thumbnailer = get_thumbnailer(obj.image)
        thumbnail_options = {'size': (200, 200)}
        return format_html(
            '<img src="/media/{0}" />'.format(
                thumbnailer.get_thumbnail(thumbnail_options)
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
        thumbnailer = get_thumbnailer(img)
        thumbnail_options = {'size': (200, 200)}
        return format_html(
            '<img src="/media/{0}" />'.format(
                thumbnailer.get_thumbnail(thumbnail_options)
            )
        )

    class Meta:
        abstract = True


class AbstractQuoteAdmin(AbstractComponentAdmin):
    readonly_fields = ['current_image']

    def current_image(self, obj):
        thumbnailer = get_thumbnailer(obj.image)
        thumbnail_options = {'size': (200, 200)}
        return format_html(
            '<img src="/media/{0}" />'.format(
                thumbnailer.get_thumbnail(thumbnail_options)
            )
        )

    class Meta:
        abstract = True


class AbstractTableAdmin(AbstractComponentAdmin):
    class Meta:
        abstract = True
