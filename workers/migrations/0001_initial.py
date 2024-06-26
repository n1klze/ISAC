# Generated by Django 5.0.6 on 2024-05-26 08:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('brigade', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('modified_at', models.DateField(auto_now=True)),
                ('brigade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='brigade.brigade')),
            ],
        ),
        migrations.CreateModel(
            name='Assembler',
            fields=[
                ('worker_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='workers.worker')),
                ('assembly_machine', models.CharField(max_length=255)),
            ],
            bases=('workers.worker',),
        ),
        migrations.CreateModel(
            name='Mechanic',
            fields=[
                ('worker_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='workers.worker')),
            ],
            bases=('workers.worker',),
        ),
        migrations.CreateModel(
            name='Terchnician',
            fields=[
                ('worker_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='workers.worker')),
            ],
            bases=('workers.worker',),
        ),
        migrations.CreateModel(
            name='Welder',
            fields=[
                ('worker_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='workers.worker')),
                ('welding_machine', models.CharField(max_length=255)),
            ],
            bases=('workers.worker',),
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('worker_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='workers.worker')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
            bases=('workers.worker',),
        ),
    ]
