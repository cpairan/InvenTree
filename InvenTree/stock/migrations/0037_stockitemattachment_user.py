# Generated by Django 3.0.5 on 2020-05-12 10:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stock', '0036_stockitemattachment'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockitemattachment',
            name='user',
            field=models.ForeignKey(blank=True, help_text='User', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
