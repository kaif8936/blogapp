# Generated by Django 2.2.6 on 2020-01-16 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(default='', max_length=50000),
        ),
    ]
