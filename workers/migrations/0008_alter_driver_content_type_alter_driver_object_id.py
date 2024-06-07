# Generated by Django 5.0.6 on 2024-06-04 16:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('workers', '0007_alter_driver_content_type_alter_driver_object_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='content_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='object_id',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
