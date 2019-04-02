# Generated by Django 2.0.9 on 2018-10-26 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0010_mybankdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Shedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_name', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
    ]
