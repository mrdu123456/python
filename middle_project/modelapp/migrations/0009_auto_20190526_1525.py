# Generated by Django 2.0.6 on 2019-05-26 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modelapp', '0008_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='b_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='b_number',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='d_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='formats',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='ibsn',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='m_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='pack',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='page',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='page_number',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='parent_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='modelapp.Sort'),
        ),
        migrations.AlterField(
            model_name='book',
            name='pb_house',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='pb_number',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='pb_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='pic',
            field=models.ImageField(null=True, upload_to='pic'),
        ),
    ]
