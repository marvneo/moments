# Generated by Django 4.0 on 2022-01-26 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('dwitter', '0002_dweer'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Dweer',
            new_name='Dweet',
        ),
    ]
