# Generated by Django 3.0.2 on 2020-04-24 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0004_auto_20200424_1123'),
    ]

    operations = [
        migrations.CreateModel(
            name='activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='img')),
                ('introduce', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='missions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dzb_name', models.CharField(max_length=20)),
                ('mission_name', models.CharField(max_length=100)),
                ('missions_principle', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='stu_img')),
                ('major_in', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('position', models.CharField(max_length=20)),
            ],
        ),
    ]
