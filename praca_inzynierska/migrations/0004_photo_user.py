# Generated by Django 2.2.5 on 2019-10-07 06:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('praca_inzynierska', '0003_auto_20191005_0538'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
