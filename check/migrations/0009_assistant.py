# Generated by Django 3.0.2 on 2020-05-25 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0008_downloadsfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='assistant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='stu_img', verbose_name='学生图片')),
                ('name', models.CharField(max_length=30, verbose_name='姓名')),
            ],
            options={
                'verbose_name': '党建服务小组',
                'verbose_name_plural': '党建服务小组',
            },
        ),
    ]