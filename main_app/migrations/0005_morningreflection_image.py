# Generated by Django 5.1.4 on 2024-12-14 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_rename_best_case_scenario_bestcasescenario_best_case_scenario_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='morningreflection',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='morning_reflections/'),
        ),
    ]