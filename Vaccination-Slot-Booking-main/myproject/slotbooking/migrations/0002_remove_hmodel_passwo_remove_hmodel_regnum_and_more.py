# Generated by Django 4.0.5 on 2022-09-10 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slotbooking', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hmodel',
            name='passwo',
        ),
        migrations.RemoveField(
            model_name='hmodel',
            name='regnum',
        ),
        migrations.AddField(
            model_name='hmodel',
            name='addr',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='hmodel',
            name='email',
            field=models.EmailField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='hmodel',
            name='hname',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
