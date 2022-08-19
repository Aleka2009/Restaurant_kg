from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from about_us.models import AboutUs, Contacts


@admin.register(AboutUs)
class AboutUsAdmin(TranslationAdmin):
    readonly_fields = ['id']
    list_display = ['name', 'description']


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    readonly_fields = ['id']
    list_display = ['phone_number', 'email', 'instagram']
