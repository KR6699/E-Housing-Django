# Generated by Django 3.1.7 on 2021-10-10 04:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminpart', '0013_auto_20211010_0957'),
    ]

    operations = [
        migrations.RenameField(
            model_name='housedetail',
            old_name='type',
            new_name='Type',
        ),
    ]
