# Generated by Django 5.0 on 2023-12-22 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='estimation',
            new_name='estimation_id',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='object',
            new_name='object_id',
        ),
    ]