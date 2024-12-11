from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import MorningReflection, EveningReflection, BestCaseScenario

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required. You cant sign a letter without a name.')
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']

class MorningReflectionForm(forms.ModelForm):
    class Meta:
        model = MorningReflection
        fields = ['grateful_for', 'what_would_make_today_great', 'daily_affirmation']

class EveningReflectionForm(forms.ModelForm):
    class Meta:
        model = EveningReflection
        fields = ['highlights_of_the_day', 'what_i_learned_today']

class BestCaseScenarioForm(forms.ModelForm):
    class Meta:
        model = BestCaseScenario
        fields = ['best_case_scenario']
