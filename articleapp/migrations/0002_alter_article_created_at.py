# Generated by Django 4.0 on 2021-12-22 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articleapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
