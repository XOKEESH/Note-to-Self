from django import forms
from .models import MorningReflection, EveningReflection, BestCaseScenario

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
