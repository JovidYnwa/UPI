# Generated by Django 4.1.3 on 2022-12-02 21:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentification', '0010_alter_useraccount_phone_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='phone_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='phone'),
        ),
    ]