# Generated by Django 5.0.6 on 2024-05-26 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bus',
            old_name='routes',
            new_name='route',
        ),
        migrations.RenameField(
            model_name='taxi',
            old_name='routes',
            new_name='route',
        ),
    ]
