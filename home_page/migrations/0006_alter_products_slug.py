# Generated by Django 3.2.6 on 2021-08-25 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0005_products_top_sell'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='slug',
            field=models.SlugField(blank=True, max_length=300, null=True, unique=True),
        ),
    ]
