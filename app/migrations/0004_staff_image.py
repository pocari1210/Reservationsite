# Generated by Django 3.1.14 on 2022-05-11 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='イメージ画像'),
        ),
    ]
