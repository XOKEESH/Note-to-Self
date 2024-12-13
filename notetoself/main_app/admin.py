from django.contrib import admin
from .models import JournalEntry, MorningReflection, EveningReflection, BestCaseScenario

# Register your models here.
admin.site.register(JournalEntry)
admin.site.register(MorningReflection)
admin.site.register(EveningReflection)
admin.site.register(BestCaseScenario)