from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class JournalEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s entry on {self.date}"

# A model for morning reflection
class MorningReflection(models.Model):
    journal_entry = models.OneToOneField(JournalEntry, on_delete=models.CASCADE)
    grateful_for = models.TextField()
    what_would_make_today_great = models.TextField()
    daily_affirmation = models.TextField()

    def __str__(self):
        return f"Morning reflection for {self.journal_entry.user.username} on {self.journal_entry.date}"

# A model for evening reflection
class EveningReflection(models.Model):
    journal_entry = models.OneToOneField(JournalEntry, on_delete=models.CASCADE)
    highlights_of_the_day = models.TextField()
    what_i_learned_today = models.TextField()

    def __str__(self):
        return f"Evening reflection for {self.journal_entry.user.username} on {self.journal_entry.date}"

# A model for best-case scenario journaling
class BestCaseScenario(models.Model):
    journal_entry = models.OneToOneField(JournalEntry, on_delete=models.CASCADE)
    best_case_scenario = models.TextField()

    def __str__(self):
        return f"Best case scenario for {self.journal_entry.user.username} on {self.journal_entry.date}"
    
class ReflectionResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reflection_type = models.CharField(max_length=100) 
    gratitude_text = models.TextField() 
    gratitude_image = models.ImageField(upload_to='reflections/', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reflection_type} by {self.user.username} on {self.date_created}"