# Generated by Django 3.2.4 on 2021-06-19 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=100)),
                ('degree', models.CharField(max_length=100)),
                ('skills', models.CharField(max_length=1000)),
                ('schooling', models.CharField(max_length=500)),
                ('university', models.CharField(max_length=500)),
                ('experience', models.TextField()),
                ('projects', models.TextField()),
                ('languages', models.CharField(max_length=1000)),
                ('awards', models.TextField()),
            ],
        ),
    ]
