from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import JournalEntry, MorningReflection, EveningReflection, BestCaseScenario
from .forms import CustomUserCreationForm, MorningReflectionForm, EveningReflectionForm, BestCaseScenarioForm
import random
import datetime
import json


QUOTE_IMAGES = [
    'images/Quote1.jpg',
    'images/Quote2.jpg',
    'images/Quote3.jpg',
    'images/Quote4.jpg',
    'images/Quote5.jpg',
    'images/Quote6.jpg',
    'images/Quote7.jpg',
    'images/Quote8.jpg',
    'images/Quote9.jpg',
    'images/Quote10.jpg',
    'images/Quote11.jpg',
    'images/Quote12.jpg',
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
            user = form.save()
            user.first_name = form.cleaned_data['first_name']
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
        mood_data = {
        "bad": 2,
        "not_great": 3,
        "okay": 5,
        "good": 7,
        "great": 4,
    }
        random_quote = random.choice(QUOTE_IMAGES)
        MorningReflection_Form = MorningReflectionForm()
        EveningReflection_Form = EveningReflectionForm()
        BestCaseScenario_Form = BestCaseScenarioForm
        return render(request, 'dashboard.html', {
            'quote_image_url': random_quote,
            'MorningReflection_Form': MorningReflection_Form,
            'EveningReflection_Form': EveningReflection_Form,
            'BestCaseScenario_Form' : BestCaseScenario_Form,
            'mood_data': json.dumps(mood_data, cls=DjangoJSONEncoder),
        })
    else:
        return redirect('login')

@login_required
def settings(request):
    return render(request, 'settings.html')

@login_required
def JournalEntry_index(request):
    journal_entries = JournalEntry.objects.filter(user=request.user)
    morning_reflection = MorningReflection.objects.filter(user=request.user)
    evening_reflection = EveningReflection.objects.filter(user=request.user)
    bestcase_scenario = BestCaseScenario.objects.filter(user=request.user)
    return render(request, 'journal_entries/index.html', 
                  {'journal_entries': journal_entries,
                   'morning_reflection': morning_reflection,
                    'evening_reflection': evening_reflection,
                    'bestcase_scenario': bestcase_scenario
                   })

@login_required
def JournalEntry_detail(request, journal_entries_id):
    journal_entry = JournalEntry.objects.get(id=journal_entries_id)
    return render(request, 'journal_entries/detail.html', {'journal_entry': journal_entry})

@login_required
def MorningReflection_detail(request, morningref_id):
    morning_reflection = MorningReflection.objects.get(id=morningref_id)
    return render(request, 'morning_reflection/detail.html', {'reflection': morning_reflection})

@login_required
def MorningReflection_confirmation(request):
    return render(request, 'morning_reflection/confirmation.html', {'user': request.user})

@login_required
def EveningReflection_detail(request, eveningref_id):
    evening_reflection = EveningReflection.objects.get(id=eveningref_id)
    return render(request, 'evening_reflection/detail.html', {'reflection': evening_reflection})

@login_required
def EveningReflection_confirmation(request):
    return render(request, 'evening_reflection/confirmation.html', {'user': request.user})

@login_required
def BestCaseScenario_detail(request, bestcase_id):
    bestcase_scenario = BestCaseScenario.objects.get(id=bestcase_id)
    return render(request, 'bestcase_scenario/detail.html', {'reflection': bestcase_scenario})

@login_required
def BestCaseScenario_confirmation(request):
    return render(request, 'bestcase_scenario/confirmation.html', {'user': request.user})

def get_current_week():
    today = datetime.date.today()
    start_of_week = today - datetime.timedelta(days=today.weekday())
    return [start_of_week + datetime.timedelta(days=i) for i in range(7)]

@login_required
def dashboard_view(request):
    today = datetime.date.today()
    week_days = get_current_week()
    current_day = today.day

    return render(request, 'dashboard.html', {
        'week_days': week_days,
        'current_day': current_day,
    })

class JournalEntryCreate(LoginRequiredMixin, CreateView):
    model = JournalEntry
    fields = '__all__'
    success_url = '/journal_entries/'

class MorningReflectionCreate(LoginRequiredMixin, CreateView):
    model = MorningReflection
    fields = [
        'date',
        'Three_things_I_am_grateful_for',
        'What_would_make_today_great', 
        'Daily_affirmation',
        'Image',
        'Mood'
    ]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    success_url = '/morningreflection/confirmation/'

class MorningReflectionUpdate(LoginRequiredMixin, UpdateView):
    model = MorningReflection
    fields = [
        'date',
        'Three_things_I_am_grateful_for',
        'What_would_make_today_great', 
        'Daily_affirmation'
    ]
    success_url = '/journal_entries/'

class MorningReflectionDelete(LoginRequiredMixin, DeleteView):
    model = MorningReflection
    success_url = '/journal_entries/'


class EveningReflectionCreate(LoginRequiredMixin, CreateView):
    model = EveningReflection
    fields = [
        'date',
        'Highlights_of_the_day', 
        'What_did_I_learn_today',
        'Image',
        'Mood'
    ]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    success_url = '/eveningreflection/confirmation/'

class EveningReflectionUpdate(LoginRequiredMixin, UpdateView):
    model = EveningReflection
    fields = [
        'date',
        'Highlights_of_the_day', 
        'What_did_I_learn_today'
    ]
    success_url = '/journal_entries/'

class EveningReflectionDelete(LoginRequiredMixin, DeleteView):
    model = EveningReflection
    success_url = '/journal_entries/'


class BestCaseScenarioCreate(LoginRequiredMixin, CreateView):
    model = BestCaseScenario
    fields = [
            'date',
            'Scenario_Topic',
            'Best_case_scenario',
            ]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    success_url = '/bestcasescenario/confirmation/'

class BestCaseScenarioUpdate(LoginRequiredMixin, UpdateView):
    model = BestCaseScenario
    fields = [
            'date',
            'Best_case_scenario',
            ]
    success_url = '/journal_entries/'

class BestCaseScenarioDelete(LoginRequiredMixin, DeleteView):
    model = BestCaseScenario
    success_url = '/journal_entries/'
