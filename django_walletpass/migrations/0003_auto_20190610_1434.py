# Generated by Django 2.2 on 2019-06-10 14:34

from django.db import migrations, models
import django_walletpass.storage


class Migration(migrations.Migration):

    dependencies = [
        ('django_walletpass', '0002_auto_20190429_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pass',
            name='data',
            field=models.FileField(storage=django_walletpass.storage.WalletPassStorage(), upload_to='passes'),
        ),
    ]
