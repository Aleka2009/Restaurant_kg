from modeltranslation.translator import register, TranslationOptions
from rest.models import Selection, Restaurant, Sale, Category


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', )


@register(Selection)
class SelectionTranslationOptions(TranslationOptions):
    fields = ('name', )


@register(Sale)
class SaleTranslationOptions(TranslationOptions):
    fields = ('name', 'text', )


@register(Restaurant)
class RestaurantTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'address', 'openning_times', )
