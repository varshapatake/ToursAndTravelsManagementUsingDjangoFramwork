# Generated by Django 2.0.9 on 2018-10-16 10:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0006_packagecosts'),
    ]

    operations = [
        migrations.AddField(
            model_name='registerpackageinfo',
            name='package_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
