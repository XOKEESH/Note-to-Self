# Generated by Django 5.1.4 on 2024-12-16 03:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_rename_image_morningreflection_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='morningreflection',
            old_name='image',
            new_name='Image',
        ),
    ]
