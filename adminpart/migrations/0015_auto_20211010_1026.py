# Generated by Django 3.1.7 on 2021-10-10 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpart', '0014_auto_20211010_1016'),
    ]

    operations = [
        migrations.RenameField(
            model_name='housedetail',
            old_name='Type',
            new_name='type',
        ),
        migrations.AlterField(
            model_name='allocatehousedetail',
            name='blockno',
            field=models.PositiveIntegerField(),
        ),
    ]