# Generated by Django 4.2.7 on 2024-01-18 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reactapp', '0009_customuser_remove_appuser_groups_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='username',
            field=models.CharField(default='anonymous', max_length=150),
        ),
    ]
