# Generated by Django 2.0.6 on 2019-05-19 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelapp', '0004_sort_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='salt',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
