# Generated by Django 5.0.6 on 2024-05-28 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0004_rename_terchnician_technician'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='modified_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]