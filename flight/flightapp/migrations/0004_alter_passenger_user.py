# Generated by Django 3.2.9 on 2021-11-16 11:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flightapp', '0003_alter_passenger_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='user',
            field=models.ForeignKey(blank=True, db_column='username', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='add_passenger', to=settings.AUTH_USER_MODEL),
        ),
    ]
