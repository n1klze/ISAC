# Generated by Django 5.0.6 on 2024-06-04 12:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('workers', '0005_alter_worker_modified_at'),
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
