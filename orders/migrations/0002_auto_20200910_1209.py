# Generated by Django 3.1.1 on 2020-09-10 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='updaetd',
            new_name='updated',
        ),
    ]
