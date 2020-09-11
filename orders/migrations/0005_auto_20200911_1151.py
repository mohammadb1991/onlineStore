# Generated by Django 3.1.1 on 2020-09-11 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_coupon'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coupon',
            old_name='discost',
            new_name='discount',
        ),
        migrations.AddField(
            model_name='order',
            name='discount',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
