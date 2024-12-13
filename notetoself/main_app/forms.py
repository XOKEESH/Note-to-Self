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
        fields = [
            'Three_things_I_am_grateful_for',
            'What_would_make_today_great', 
            'Daily_affirmation'
            ]

class EveningReflectionForm(forms.ModelForm):
    class Meta:
        model = EveningReflection
        fields = [
            'Highlights_of_the_day', 
            'What_did_I_learn_today'
            ]

class BestCaseScenarioForm(forms.ModelForm):
    class Meta:
        model = BestCaseScenario
        fields = [
            'Scenario_Topic',
            'Best_case_scenario',
            ]
