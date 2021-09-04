# Generated by Django 3.2.6 on 2021-09-04 17:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home_page', '0020_auto_20210904_2306'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='cart_owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cart_owner', to=settings.AUTH_USER_MODEL),
        ),
    ]