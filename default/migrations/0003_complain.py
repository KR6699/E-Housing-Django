# Generated by Django 3.2.6 on 2021-08-12 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0002_auto_20210809_1717'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('subject', models.CharField(max_length=200)),
                ('complain', models.CharField(max_length=500)),
            ],
        ),
    ]
