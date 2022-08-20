from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class AboutUs(models.Model):
    name = models.CharField('Название', max_length=255)
    description = models.TextField('О нас')

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

    def clean(self):
        self.name = self.name.capitalize()

    def __str__(self):
        return self.name


class Contacts(models.Model):
    phone_number = PhoneNumberField('Номер телефона')
    email = models.EmailField('Почта')
    instagram = models.URLField('Ссылка на Instagram', max_length=300)

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return f'{self.phone_number}'

