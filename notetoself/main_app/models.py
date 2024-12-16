from django.db import models
from django.contrib.auth.models import User
from datetime import date


# class JournalEntry(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)  
#     date = models.DateField(auto_now_add=True)  
#     morning_reflection = models.CharField(null=True, blank=True) 
#     evening_reflection = models.CharField(null=True, blank=True)
#     best_case_scenario = models.TextField(null=True, blank=True)

#     def __str__(self):
#         return f"Journal Entry for {self.user.username} on {self.date}"  



class JournalEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s entry on {self.date}"


# A model for morning reflection
class MorningReflection(models.Model):

    MOOD_CHOICES = [
        ('bad', 'Bad'),
        ('not_great', 'Not Great'),
        ('okay', 'Okay'),
        ('good', 'Good'),
        ('great', 'Great')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    Three_things_I_am_grateful_for = models.TextField()
    What_would_make_today_great = models.TextField()
    Daily_affirmation = models.TextField()
    Image = models.ImageField(upload_to='morning_reflections/', blank=True, null=True)
    Mood = models.CharField(
        max_length=10,
        choices=MOOD_CHOICES,
        default='okay', 
        null=True
    )

    def __str__(self):
        return f"Morning reflection for {self.user.username} on {self.date}"


# A model for evening reflection
class EveningReflection(models.Model):

    MOOD_CHOICES = [
        ('bad', 'Bad'),
        ('not_great', 'Not Great'),
        ('okay', 'Okay'),
        ('good', 'Good'),
        ('great', 'Great')
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    Highlights_of_the_day = models.TextField()
    What_did_I_learn_today = models.TextField()
    Image = models.ImageField(upload_to='morning_reflections/', blank=True, null=True)
    Mood = models.CharField(
        max_length=100,
        choices=MOOD_CHOICES,
        default='okay', 
        null=True
    )

    def __str__(self):
        return f"Evening reflection for {self.user.username} on {self.date}"


# A model for best-case scenario journaling
class BestCaseScenario(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    Scenario_Topic = models.CharField(max_length=100)
    Best_case_scenario = models.TextField()

    def __str__(self):
        return f"Best case scenario for {self.user.username} on {self.date}"













class ReflectionResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reflection_type = models.CharField(max_length=100) 
    gratitude_text = models.TextField() 
    gratitude_image = models.ImageField(upload_to='reflections/', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reflection_type} by {self.user.username} on {self.date_created}"