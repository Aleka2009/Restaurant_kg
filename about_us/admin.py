from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from about_us.models import AboutUs, Contacts


@admin.register(AboutUs)
class AboutUsAdmin(TranslationAdmin):
    readonly_fields = ['id']
    list_display = ['name', 'description']

    def has_add_permission(self, request):
        if self.model.objects.count() > 0:
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    readonly_fields = ['id']
    list_display = ['phone_number', 'email', 'instagram']

    def has_add_permission(self, request):
        if self.model.objects.count() > 0:
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        return False
