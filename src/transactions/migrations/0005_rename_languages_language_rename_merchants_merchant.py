# Generated by Django 4.1.3 on 2022-12-16 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0004_merchantcategory_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Languages',
            new_name='Language',
        ),
        migrations.RenameModel(
            old_name='Merchants',
            new_name='Merchant',
        ),
    ]
