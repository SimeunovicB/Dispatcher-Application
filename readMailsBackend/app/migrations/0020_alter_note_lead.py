# Generated by Django 3.2.8 on 2021-11-05 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='lead',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.lead'),
        ),
    ]
