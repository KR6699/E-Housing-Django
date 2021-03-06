# Generated by Django 3.1.7 on 2021-08-09 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rent_List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=50)),
                ('house_no', models.PositiveIntegerField()),
                ('type', models.CharField(max_length=10)),
                ('username', models.CharField(max_length=20)),
                ('rent_price', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Sell_List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=50)),
                ('house_no', models.PositiveIntegerField()),
                ('type', models.CharField(max_length=10)),
                ('username', models.CharField(max_length=20)),
                ('sell_price', models.PositiveIntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='RentList',
        ),
        migrations.DeleteModel(
            name='SellList',
        ),
    ]
