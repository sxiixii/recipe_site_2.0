# Generated by Django 3.1.3 on 2020-11-27 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0013_auto_20201127_1941'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredient',
            old_name='name',
            new_name='title',
        ),
    ]
