# Generated by Django 3.2.4 on 2021-06-19 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='schooling',
            field=models.TextField(),
        ),
    ]