# Generated by Django 3.2.6 on 2021-08-28 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0011_cart_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='device_name',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
