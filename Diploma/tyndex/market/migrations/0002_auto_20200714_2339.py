# Generated by Django 2.2 on 2020-07-14 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(blank=True, upload_to='products/img/', verbose_name='Изображение'),
        ),
    ]
