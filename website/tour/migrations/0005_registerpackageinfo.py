# Generated by Django 2.0.9 on 2018-10-15 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0004_admininfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterPackageInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('gender', models.CharField(max_length=250)),
                ('age', models.IntegerField()),
                ('mobile', models.IntegerField()),
                ('email', models.CharField(max_length=250)),
                ('noofpeople', models.IntegerField()),
            ],
        ),
    ]
