from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import date
from .models import JournalEntry, MorningReflection, EveningReflection, BestCaseScenario
from .forms import MorningReflectionForm, EveningReflectionForm, BestCaseScenarioForm

import random

QUOTE_IMAGES = [
    'images/Quote1.jpg',
    'images/Quote2.jpg',
    'images/Quote3.jpeg',
    # Add more quotes here
]

# Create your views here.
def home(request):
    # Send a simple HTML response
    return HttpResponse('<h1>Hello, You!</h1>')

def about(request):
    return render(request, 'about.html')

def dashboard(request):
    # Randomly pick a quote image for the user
    random_quote = random.choice(QUOTE_IMAGES)
    return render(request, 'dashboard.html', {'quote_image_url': random_quote})

def settings(request):
    return render(request, 'settings.html')

# Handle Morning Reflection
def morning_reflection(request):
    user = request.user
    journal_entry, created = JournalEntry.objects.get_or_create(user=user, date=date.today())
    morning_reflection, created = MorningReflection.objects.get_or_create(journal_entry=journal_entry)

    if request.method == 'POST':
        form = MorningReflectionForm(request.POST, instance=morning_reflection)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = MorningReflectionForm(instance=morning_reflection)

    return render(request, 'morning_reflection.html', {'form': form})

# Handle Evening Reflection
def evening_reflection(request):
    user = request.user
    journal_entry, created = JournalEntry.objects.get_or_create(user=user, date=date.today())
    evening_reflection, created = EveningReflection.objects.get_or_create(journal_entry=journal_entry)

    if request.method == 'POST':
        form = EveningReflectionForm(request.POST, instance=evening_reflection)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EveningReflectionForm(instance=evening_reflection)

    return render(request, 'evening_reflection.html', {'form': form})

# Handle Best Case Scenario
def best_case_scenario(request):
    user = request.user
    journal_entry, created = JournalEntry.objects.get_or_create(user=user, date=date.today())
    best_case_scenario, created = BestCaseScenario.objects.get_or_create(journal_entry=journal_entry)

    if request.method == 'POST':
        form = BestCaseScenarioForm(request.POST, instance=best_case_scenario)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = BestCaseScenarioForm(instance=best_case_scenario)

    return render(request, 'best_case_scenario.html', {'form': form})
    
def create_or_update_morning_reflection(request):
    user = request.user
    journal_entry, created = JournalEntry.objects.get_or_create(user=user, date=date.today())

    # Check if the morning reflection already exists
    morning_reflection, created = MorningReflection.objects.get_or_create(journal_entry=journal_entry)

    if request.method == 'POST':
        # Handle form submission
        form = MorningReflectionForm(request.POST, instance=morning_reflection)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = MorningReflectionForm(instance=morning_reflection)

    return render(request, 'morning_reflection.html', {'form': form})

def create_or_update_evening_reflection(request):
    user = request.user
    journal_entry, created = JournalEntry.objects.get_or_create(user=user, date=date.today())

    # Check if the evening reflection already exists
    evening_reflection, created = EveningReflection.objects.get_or_create(journal_entry=journal_entry)

    if request.method == 'POST':
        # Handle form submission
        form = EveningReflectionForm(request.POST, instance=evening_reflection)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EveningReflectionForm(instance=evening_reflection)

    return render(request, 'evening_reflection.html', {'form': form})

def create_or_update_best_case_scenario(request):
    user = request.user
    journal_entry, created = JournalEntry.objects.get_or_create(user=user, date=date.today())

    # Check if the best case scenario entry already exists
    best_case_scenario, created = BestCaseScenario.objects.get_or_create(journal_entry=journal_entry)

    if request.method == 'POST':
        # Handle form submission
        form = BestCaseScenarioForm(request.POST, instance=best_case_scenario)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = BestCaseScenarioForm(instance=best_case_scenario)

    return render(request, 'best_case_scenario.html', {'form': form})