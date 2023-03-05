# Generated by Django 4.1.3 on 2023-03-05 19:59

import base.services
import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentification', '0015_userdata_user_email_alter_userdata_user_passport'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankLogos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('merch_id', models.CharField(blank=True, max_length=50, null=True)),
                ('merchat_name', models.CharField(max_length=200)),
                ('merchant_description', models.TextField(blank=True, null=True)),
                ('start_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('end_date', models.DateTimeField(default=datetime.datetime(2999, 12, 1, 0, 0))),
                ('merchant_logo', models.ImageField(blank=True, null=True, upload_to=base.services.get_path_upload_merchant, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg']), base.services.validate_size_image])),
                ('lang_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.language')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partner_transaction_id', models.CharField(blank=True, max_length=100, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('start_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentification.useraccount')),
                ('merchant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.merchant')),
            ],
        ),
        migrations.CreateModel(
            name='MerchantCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
                ('start_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('end_date', models.DateTimeField(default=datetime.datetime(2999, 12, 1, 0, 0, tzinfo=datetime.timezone.utc))),
                ('category_logo', models.ImageField(blank=True, null=True, upload_to=base.services.get_path_upload_merchant, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg']), base.services.validate_size_image])),
                ('lang_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.language')),
            ],
        ),
        migrations.AddField(
            model_name='merchant',
            name='merch_cat_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.merchantcategory'),
        ),
    ]
