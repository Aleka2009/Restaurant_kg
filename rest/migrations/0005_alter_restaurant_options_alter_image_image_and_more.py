# Generated by Django 4.1 on 2022-08-23 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0004_category_remove_restaurant_bars_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='restaurant',
            options={'verbose_name': 'Заведение', 'verbose_name_plural': 'Заведения'},
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image_rest/', verbose_name='Изображения'),
        ),
        migrations.AlterField(
            model_name='menuimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='menu_image_rest/', verbose_name='Изображения'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='logo/', verbose_name='Логотип'),
        ),
        migrations.AlterField(
            model_name='saleimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='sale_image/', verbose_name='Изображения'),
        ),
        migrations.AlterField(
            model_name='selection',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='selections_image/', verbose_name='Фото'),
        ),
    ]
