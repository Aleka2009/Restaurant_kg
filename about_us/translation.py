from modeltranslation.translator import register, TranslationOptions
from about_us.models import AboutUs


@register(AboutUs)
class AboutUsTranslationOptions(TranslationOptions):
    fields = ('name', 'description', )

