# Generated by Django 5.0.6 on 2024-05-26 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0004_alter_vehicle_created_at_alter_vehicle_modified_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='modified_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]