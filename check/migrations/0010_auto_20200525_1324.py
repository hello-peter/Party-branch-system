# Generated by Django 3.0.2 on 2020-05-25 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0009_assistant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assistant',
            name='img',
            field=models.ImageField(upload_to='assis_img', verbose_name='学生图片'),
        ),
    ]