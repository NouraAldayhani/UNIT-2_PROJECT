# Generated by Django 4.2.1 on 2023-06-06 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_contact_created_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='created_date',
        ),
    ]