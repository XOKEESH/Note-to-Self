from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from datetime import date
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import JournalEntry, MorningReflection, EveningReflection, BestCaseScenario, ReflectionResponse  
from .forms import CustomUserCreationForm, MorningReflectionForm, EveningReflectionForm, BestCaseScenarioForm
import random

QUOTE_IMAGES = [
    'images/Quote1.jpg',
    'images/Quote2.jpg',
    'images/Quote3.jpeg',
]

# Create your views here.
class home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.save()
            login(request, user)
            return redirect('dashboard')
        else:
            error_message = 'Invalid sign up - try again'
    else:
        form = CustomUserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

@login_required
def dashboard(request):
    if request.user.is_authenticated:
        # Randomly pick a quote image for the user
        random_quote = random.choice(QUOTE_IMAGES)
        reflections = ReflectionResponse.objects.filter(user=request.user).order_by('-date_created')
        return render(request, 'dashboard.html', {
            'quote_image_url': random_quote,
            'reflections': reflections
        })
    else:
        return redirect('login')

def settings(request):
    return render(request, 'settings.html')

@login_required
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

@login_required
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

@login_required
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


@login_required
def create_or_update_morning_reflection(request):
    user = request.user
    journal_entry, created = JournalEntry.objects.get_or_create(user=user, date=date.today())
    morning_reflection, created = MorningReflection.objects.get_or_create(journal_entry=journal_entry)

    if request.method == 'POST':
        form = MorningReflectionForm(request.POST, instance=morning_reflection)
        if form.is_valid():
            form.save()

            gratitude_text = request.POST.get('gratitude-1')
            gratitude_image = request.FILES.get('reflection-image')

            reflection = ReflectionResponse(
                user=request.user,
                reflection_type='morning',
                gratitude_text=gratitude_text,
                gratitude_image=gratitude_image
            )
            reflection.save()

            return redirect('dashboard')
    else:
        form = MorningReflectionForm(instance=morning_reflection)

    return render(request, 'morning_reflection.html', {'form': form})

@login_required
def create_or_update_evening_reflection(request):
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

@login_required
def create_or_update_best_case_scenario(request):
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