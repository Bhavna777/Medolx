# Generated by Django 2.2 on 2021-06-03 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medolx', '0012_auto_20210603_1903'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='patient',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='patient',
            new_name='user',
        ),
    ]
