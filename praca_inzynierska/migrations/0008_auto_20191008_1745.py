# Generated by Django 2.2.5 on 2019-10-08 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('praca_inzynierska', '0007_actor'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='name',
            field=models.CharField(default='name', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='actor',
            name='surname',
            field=models.CharField(default='surname', max_length=100),
            preserve_default=False,
        ),
    ]
