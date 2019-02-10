from factory import RelatedFactory, SubFactory
from factory.django import ImageField
from factory.fuzzy import FuzzyText
from factory_djoy import CleanModelFactory

from ..models import Gallery, Image, Thumbnail


class ThumbnailFactory(CleanModelFactory):
    image = ImageField()

    class Meta:
        model = Thumbnail


class GalleryFactory(CleanModelFactory):
    title = FuzzyText()
    summary = FuzzyText()

    RelatedFactory(ThumbnailFactory, 'gallery')

    class Meta:
        model = Gallery


class ImageFactory(CleanModelFactory):
    caption = FuzzyText()
    image = ImageField()
    gallery = SubFactory(GalleryFactory)

    class Meta:
        model = Image
