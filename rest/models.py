from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from custom_auth.models import MyUser


class Category(models.Model):
    """Категории"""
    name = models.CharField(verbose_name='Название', max_length=255)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def clean(self):
        self.name = self.name.capitalize()

    def __str__(self):
        return self.name


class Selection(models.Model):
    """Подборки"""
    name = models.CharField('Название', max_length=255)
    image = models.ImageField('Фото', upload_to="selections_image/", blank=True, null=True)

    class Meta:
        verbose_name = 'Подборка'
        verbose_name_plural = 'Подборки'

    def clean(self):
        self.name = self.name.capitalize()

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    """Все заведения"""
    logo = models.ImageField('Логотип', upload_to='logo/', blank=True, null=True)
    name = models.CharField('Название', max_length=255)
    description = models.TextField('Описание')
    address = models.CharField('Местоположение', max_length=255)
    openning_times = models.CharField('Время работы', max_length=255)
    selection = models.ManyToManyField(Selection, blank=True, verbose_name='Подборки')
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.SET_NULL,
                                 null=True, blank=True)
    # user = models.ManyToManyField(MyUser, through='Rating', related_name='rest')
    favorite = models.ManyToManyField(MyUser, through='Favorite', related_name='favorite')
    # fav = models.BooleanField()
    instagram = models.URLField('Сcылка на Instagram', max_length=300, blank=True, null=True)
    site = models.URLField('Ссылка на сайт', max_length=300, blank=True, null=True)

    def clean(self):
        self.name = self.name.capitalize()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заведение'
        verbose_name_plural = 'Заведения'


class Contact(models.Model):
    """Контакты"""
    phone_number = PhoneNumberField('Номер телефона')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE,
                                   related_name='phone_numbers', verbose_name='Заведение')

    def __str__(self):
        return f'{self.phone_number}'

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'


class Sale(models.Model):
    """Акции"""
    time_create = models.DateTimeField('Дата добавления', auto_now_add=True)
    time_update = models.DateTimeField('Дата обновления', auto_now=True)
    name = models.CharField('Афиша', max_length=255)
    text = models.TextField('Описание')
    restaurant = models.ForeignKey(Restaurant, verbose_name='Заведение', on_delete=models.CASCADE)

    def clean(self):
        self.name = self.name.capitalize()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'


class SaleImage(models.Model):
    image = models.ImageField('Изображения', upload_to='sale_image/', blank=True, null=True)
    sale_image = models.ForeignKey(Sale, related_name='sale_image', verbose_name='Фото',
                                   on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'


class Image(models.Model):
    image = models.ImageField('Изображения', upload_to='image_rest/', blank=True, null=True)
    restaurant = models.ForeignKey(Restaurant, related_name='image', verbose_name='Фото',
                                   on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Фотография ресторана'
        verbose_name_plural = 'Фотографии ресторана'


class MenuImage(models.Model):
    image = models.ImageField('Изображения', upload_to='menu_image_rest/', blank=True, null=True)
    restaurant = models.ForeignKey(Restaurant, related_name='menu_image', verbose_name='Фото',
                                   on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Фотография меню'
        verbose_name_plural = 'Фотографии меню'


class Review(models.Model):
    """Отзывы"""
    user = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True)
    text = models.TextField('Содержание отзыва')
    restaurant = models.ForeignKey(Restaurant, related_name='review', on_delete=models.CASCADE)

    def clean(self):
        self.name = self.name.capitalize()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Rating(models.Model):
    """Рейтинг"""

    RATE_CHOICES = (
        (1, '1'), (2, '2'),
        (3, '3'), (4, '4'),
        (5, '5'), (6, '6'),
        (7, '7'), (8, '8'),
        (9, '9'), (10, '10'),
    )
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, verbose_name='пользователь')
    rate = models.FloatField('Рейтинг', choices=RATE_CHOICES, null=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, verbose_name='ресторан', related_name='rate')

    def __str__(self):
        return f'{self.rate} - {self.restaurant.name} by {self.user.email}'

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'
        unique_together = (('user', 'restaurant'),)


class Favorite(models.Model):
    """Избранное"""
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE,
                             verbose_name='пользователь', related_name='favorite_user')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, verbose_name='ресторан',
                                   related_name='restaurant_list')

