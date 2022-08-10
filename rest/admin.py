from django.contrib import admin
from django.contrib.admin.options import TabularInline
from rest.models import Category, Selection, Sale, Restaurant, Image, MenuImage, SaleImage, Rating


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
class CategoryModelAdmin(admin.ModelAdmin):
    readonly_fields = ['id']
    list_display = ['name']


@admin.register(Selection)
class SelectionModelAdmin(admin.ModelAdmin):
    readonly_fields = ['id']
    list_display = ['name']


@admin.register(Sale)
class SaleModelAdmin(admin.ModelAdmin):
    inlines = (SaleImageAdminInLine, )
    readonly_fields = ['id']
    list_display = ['name', 'time_create', 'time_update', ]


@admin.register(Restaurant)
class RestaurantModelAdmin(admin.ModelAdmin):
    inlines = (RestaurantImageAdminInline, RestaurantMenuImageAdminInLine)
    readonly_fields = ['id']
    list_display = ['name', 'phone_number_1', ]


@admin.register(Rating)
class MyUserRatingAdmin(admin.ModelAdmin):
    pass

