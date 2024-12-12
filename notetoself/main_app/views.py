from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import JournalEntry

from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.http import JsonResponse
from datetime import date
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
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

def JournalEntry_index(request):
    journal_entries = JournalEntry.objects.all()
    return render(request, 'journal_entries/index.html', {'journal_entries': journal_entries})

def JournalEntry_detail(request, journal_entries_id):
    journal_entry = JournalEntry.objects.get(id=journal_entries_id)
    return render(request, 'journal_entries/detail.html', {'journal_entry': journal_entry})

# class Journal_Entries_Create(CreateView)
    
class JournalEntryCreate(CreateView):
    model = JournalEntry
    fields = '__all__'
    success_url = '/journal_entries/'






# Saving or Updating a Reflection
# class SaveReflectionView(LoginRequiredMixin, View):
#     def post(self, request):
#         user = request.user
#         reflection_type = request.POST.get('reflection_type')  # 'morning_reflection', 'evening_reflection', or 'best_case_scenario'
#         answers = request.POST.get('answers')  # JSON string for reflections

#         if reflection_type not in ['morning_reflection', 'evening_reflection', 'best_case_scenario']:
#             return JsonResponse({'error': 'Invalid reflection type'}, status=400)

#         # Check if today's entry already exists
#         journal_entry, created = JournalEntry.objects.get_or_create(user=user, date=date.today())

#         # Update the appropriate reflection
#         if reflection_type == 'morning_reflection':
#             journal_entry.morning_reflection = answers
#         elif reflection_type == 'evening_reflection':
#             journal_entry.evening_reflection = answers
#         elif reflection_type == 'best_case_scenario':
#             journal_entry.best_case_scenario = answers

#         journal_entry.save()
#         return JsonResponse({'message': 'Reflection saved successfully', 'created': created})
    
# 
# class JournalListView(LoginRequiredMixin, ListView):
#     model = JournalEntry
#     template_name = 'journalEntries.html'  # Create this template
#     context_object_name = 'journal_entries'

#     def get_queryset(self):
#         return JournalEntry.objects.filter(user=self.request.user).order_by('-date')

# main_app/views.py

# class JournalEntry:
#     def __init__(self, date):
#         self.date = date

# @login_required
# def morning_reflection(request):
#     user = request.user
#     journal_entry, created = JournalEntry.objects.get_or_create(user=user, date=date.today())
#     morning_reflection, created = MorningReflection.objects.get_or_create(journal_entry=journal_entry)

#     if request.method == 'POST':
#         form = MorningReflectionForm(request.POST, instance=morning_reflection)
#         if form.is_valid():
#             form.save()
#             return redirect('dashboard')
#     else:
#         form = MorningReflectionForm(instance=morning_reflection)

#     return render(request, 'morning_reflection.html', {'form': form})

# @login_required
# def evening_reflection(request):
#     user = request.user
#     journal_entry, created = JournalEntry.objects.get_or_create(user=user, date=date.today())
#     evening_reflection, created = EveningReflection.objects.get_or_create(journal_entry=journal_entry)

#     if request.method == 'POST':
#         form = EveningReflectionForm(request.POST, instance=evening_reflection)
#         if form.is_valid():
#             form.save()
#             return redirect('dashboard')
#     else:
#         form = EveningReflectionForm(instance=evening_reflection)

#     return render(request, 'evening_reflection.html', {'form': form})

# @login_required
# def best_case_scenario(request):
#     user = request.user
#     journal_entry, created = JournalEntry.objects.get_or_create(user=user, date=date.today())
#     best_case_scenario, created = BestCaseScenario.objects.get_or_create(journal_entry=journal_entry)

#     if request.method == 'POST':
#         form = BestCaseScenarioForm(request.POST, instance=best_case_scenario)
#         if form.is_valid():
#             form.save()
#             return redirect('dashboard')
#     else:
#         form = BestCaseScenarioForm(instance=best_case_scenario)

#     return render(request, 'best_case_scenario.html', {'form': form})


# @login_required
# def create_or_update_morning_reflection(request):
#     user = request.user
#     journal_entry, created = JournalEntry.objects.get_or_create(user=user, date=date.today())
#     morning_reflection, created = MorningReflection.objects.get_or_create(journal_entry=journal_entry)

#     if request.method == 'POST':
#         form = MorningReflectionForm(request.POST, instance=morning_reflection)
#         if form.is_valid():
#             form.save()

#             gratitude_text = request.POST.get('gratitude-1')
#             gratitude_image = request.FILES.get('reflection-image')

#             reflection = ReflectionResponse(
#                 user=request.user,
#                 reflection_type='morning',
#                 gratitude_text=gratitude_text,
#                 gratitude_image=gratitude_image
#             )
#             reflection.save()

#             return redirect('dashboard')
#     else:
#         form = MorningReflectionForm(instance=morning_reflection)

#     return render(request, 'morning_reflection.html', {'form': form})

# @login_required
# def create_or_update_evening_reflection(request):
#     user = request.user
#     journal_entry, created = JournalEntry.objects.get_or_create(user=user, date=date.today())

#     evening_reflection, created = EveningReflection.objects.get_or_create(journal_entry=journal_entry)

#     if request.method == 'POST':
#         form = EveningReflectionForm(request.POST, instance=evening_reflection)
#         if form.is_valid():
#             form.save()
#             return redirect('dashboard')
#     else:
#         form = EveningReflectionForm(instance=evening_reflection)

#     return render(request, 'evening_reflection.html', {'form': form})

# @login_required
# def create_or_update_best_case_scenario(request):
#     user = request.user
#     journal_entry, created = JournalEntry.objects.get_or_create(user=user, date=date.today())

#     best_case_scenario, created = BestCaseScenario.objects.get_or_create(journal_entry=journal_entry)

#     if request.method == 'POST':
#         form = BestCaseScenarioForm(request.POST, instance=best_case_scenario)
#         if form.is_valid():
#             form.save()
#             return redirect('dashboard')
#     else:
#         form = BestCaseScenarioForm(instance=best_case_scenario)

#     return render(request, 'best_case_scenario.html', {'form': form})

