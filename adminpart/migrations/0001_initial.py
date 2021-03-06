# Generated by Django 3.1.7 on 2021-07-23 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SocietyDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=256)),
                ('city', models.CharField(max_length=50)),
                ('pincode', models.PositiveIntegerField()),
                ('nohouse', models.PositiveIntegerField()),
                ('image', models.FileField(upload_to='upload_society_imgs')),
            ],
        ),
    ]
