# Generated by Django 2.2.5 on 2019-10-05 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('praca_inzynierska', '0002_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
    ]
