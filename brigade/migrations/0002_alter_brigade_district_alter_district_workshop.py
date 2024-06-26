# Generated by Django 5.0.6 on 2024-06-04 17:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brigade', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brigade',
            name='district',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='brigade.district'),
        ),
        migrations.AlterField(
            model_name='district',
            name='workshop',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='brigade.workshop'),
        ),
    ]
