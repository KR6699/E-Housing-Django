# Generated by Django 3.1.7 on 2021-07-25 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminpart', '0004_allocatehousedetail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allocatehousedetail',
            name='entry_date',
        ),
    ]