# Generated by Django 2.0.6 on 2019-05-23 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modelapp', '0006_auto_20190519_1800'),
    ]

    operations = [
        migrations.CreateModel(
            name='Confirm_string',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=256)),
                ('code_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 't_confirm_string',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='confirm_string',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelapp.User'),
        ),
    ]