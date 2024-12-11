# Generated by Django 5.1.4 on 2024-12-11 01:24

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='JournalEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EveningReflection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('highlights_of_the_day', models.TextField()),
                ('what_i_learned_today', models.TextField()),
                ('journal_entry', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_app.journalentry')),
            ],
        ),
        migrations.CreateModel(
            name='BestCaseScenario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('best_case_scenario', models.TextField()),
                ('journal_entry', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_app.journalentry')),
            ],
        ),
        migrations.CreateModel(
            name='MorningReflection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grateful_for', models.TextField()),
                ('what_would_make_today_great', models.TextField()),
                ('daily_affirmation', models.TextField()),
                ('journal_entry', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_app.journalentry')),
            ],
        ),
    ]
