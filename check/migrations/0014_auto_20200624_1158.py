# Generated by Django 3.0.7 on 2020-06-24 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0013_auto_20200624_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact_us',
            name='connect',
            field=models.CharField(default='tel/e-mail', max_length=50, verbose_name='邮箱/电话'),
        ),
        migrations.AlterField(
            model_name='contact_us',
            name='comments',
            field=models.CharField(default='contents', max_length=500, verbose_name='留言内容'),
        ),
        migrations.AlterField(
            model_name='contact_us',
            name='name',
            field=models.CharField(default='name', max_length=50, verbose_name='留言者名字'),
        ),
    ]