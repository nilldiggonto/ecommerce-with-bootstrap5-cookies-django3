# Generated by Django 3.2.6 on 2021-09-12 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0021_cart_cart_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='main_shop',
            field=models.BooleanField(default=False),
        ),
    ]
