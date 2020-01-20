# Generated by Django 3.0.2 on 2020-01-20 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20200120_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='address_line',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Address'),
        ),
        migrations.AddField(
            model_name='contact',
            name='city',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='City'),
        ),
        migrations.AddField(
            model_name='contact',
            name='postcode',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Post/Zip-code'),
        ),
        migrations.AddField(
            model_name='contact',
            name='state',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='State'),
        ),
        migrations.AddField(
            model_name='contact',
            name='street',
            field=models.CharField(blank=True, max_length=55, null=True, verbose_name='Street'),
        ),
    ]
