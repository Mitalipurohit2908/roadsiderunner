# Generated by Django 4.1.7 on 2023-04-14 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_alter_booking_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='sprovider_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='sprovider_phone',
            field=models.CharField(max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='lang',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='booking',
            name='lat',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='serviceprovider',
            name='lang',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='serviceprovider',
            name='lat',
            field=models.CharField(max_length=100),
        ),
    ]
