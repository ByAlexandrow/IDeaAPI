# Generated by Django 3.2.16 on 2024-01-24 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_auto_20240125_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]
