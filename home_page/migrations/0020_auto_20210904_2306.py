# Generated by Django 3.2.6 on 2021-09-04 17:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home_page', '0019_alter_products_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shop_owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='address_two',
            field=models.TextField(blank=True, null=True),
        ),
    ]