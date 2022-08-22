from django.contrib import admin
from django.contrib.admin.options import TabularInline
from modeltranslation.admin import TranslationAdmin

from rest.models import Selection, Sale, Restaurant, Image, MenuImage, SaleImage, Rating, Contact, Category


class ContactAdminInLine(TabularInline):
    model = Contact


class SaleImageAdminInLine(TabularInline):
    extra = 1
    model = SaleImage
    max_num = 100


class RestaurantMenuImageAdminInLine(TabularInline):
    extra = 1
    model = MenuImage
    max_num = 100


class RestaurantImageAdminInline(TabularInline):
    extra = 1
    model = Image
    max_num = 100


@admin.register(Category)
class CategoryModelAdmin(TranslationAdmin):
    readonly_fields = ['id']
    list_display = ['name']


@admin.register(Selection)
class SelectionModelAdmin(TranslationAdmin):
    readonly_fields = ['id']
    list_display = ['name']


@admin.register(Sale)
class SaleModelAdmin(TranslationAdmin):
    inlines = (SaleImageAdminInLine, )
    readonly_fields = ['id']
    list_display = ['name', 'time_create', 'time_update', ]


@admin.register(Restaurant)
class RestaurantModelAdmin(TranslationAdmin):
    inlines = (RestaurantImageAdminInline, RestaurantMenuImageAdminInLine, ContactAdminInLine)
    readonly_fields = ['id']
    list_display = ['name', 'description', ]


@admin.register(Rating)
class MyUserRatingAdmin(admin.ModelAdmin):
    pass


@admin.register(Contact)
class ContactsAdmin(admin.ModelAdmin):
    pass
