# Generated by Django 3.2.8 on 2021-11-02 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20211102_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='email',
            field=models.CharField(default='', max_length=254, unique=True),
            preserve_default=False,
        ),
    ]
