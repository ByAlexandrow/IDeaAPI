# Generated by Django 3.2.16 on 2024-01-25 08:06

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0011_alter_group_title'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='unique_following_user_following',
        ),
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together={('user', 'following')},
        ),
    ]
