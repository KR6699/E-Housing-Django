# Generated by Django 3.1.7 on 2021-10-10 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpart', '0015_auto_20211010_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allocatehousedetail',
            name='sname',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='housedetail',
            name='sname',
            field=models.CharField(max_length=50),
        ),
    ]
