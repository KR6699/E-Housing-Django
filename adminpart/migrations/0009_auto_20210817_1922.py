# Generated by Django 3.1.7 on 2021-08-17 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpart', '0008_auto_20210808_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allocatehousedetail',
            name='mobile_no',
            field=models.PositiveBigIntegerField(),
        ),
    ]