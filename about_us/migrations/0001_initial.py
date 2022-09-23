# Generated by Django 4.1.1 on 2022-09-23 13:11

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('name_ru', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('name_en', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('name_ky', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('description', models.TextField(verbose_name='О нас')),
                ('description_ru', models.TextField(null=True, verbose_name='О нас')),
                ('description_en', models.TextField(null=True, verbose_name='О нас')),
                ('description_ky', models.TextField(null=True, verbose_name='О нас')),
            ],
            options={
                'verbose_name': 'О нас',
                'verbose_name_plural': 'О нас',
            },
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('instagram', models.URLField(max_length=300, verbose_name='Ссылка на Instagram')),
            ],
            options={
                'verbose_name': 'Контакты',
                'verbose_name_plural': 'Контакты',
            },
        ),
    ]
