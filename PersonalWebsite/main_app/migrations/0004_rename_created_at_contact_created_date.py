# Generated by Django 4.2.1 on 2023-06-06 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_project_project_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='created_at',
            new_name='created_date',
        ),
    ]