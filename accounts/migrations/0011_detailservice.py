# Generated by Django 4.1.7 on 2023-04-11 21:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0010_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detailservice',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('phone', models.CharField(max_length=13)),
                ('lat', models.FloatField()),
                ('lang', models.FloatField()),
                ('service_type', models.CharField(choices=[('as_a', 'AS A'), ('mechanic', 'MECHANIC'), ('fual_station', 'FUAL STATION')], default='as_a', max_length=15)),
                ('service_name', models.TextField()),
                ('address', models.TextField()),
                ('pincode', models.IntegerField()),
                ('profile', models.ImageField(upload_to='photos/services')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('userprofile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.userprofile')),
            ],
        ),
    ]
