# Generated by Django 3.2.4 on 2021-06-20 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_auto_20210620_1217'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='tenth_score',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='resume',
            name='twelveth_score',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='resume',
            name='university_score',
            field=models.CharField(default='', max_length=10),
        ),
    ]