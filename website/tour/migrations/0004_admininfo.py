# Generated by Django 2.0.9 on 2018-10-11 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0003_auto_20181005_1124'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('age', models.IntegerField()),
                ('mobile', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
    ]
