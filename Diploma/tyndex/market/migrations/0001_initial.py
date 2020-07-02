# Generated by Django 2.2.10 on 2020-07-02 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.PositiveIntegerField()),
                ('product_number', models.PositiveIntegerField()),
                ('img', models.FileField(upload_to='products\\%Y%m%d')),
            ],
        ),
    ]
