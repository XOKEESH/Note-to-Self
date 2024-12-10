from django.shortcuts import render, redirect
from django.http import HttpResponse
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
    if request.method == 'POST':
        gratitude_1 = request.POST.get('gratitude-1')
        gratitude_2 = request.POST.get('gratitude-2')
        gratitude_3 = request.POST.get('gratitude-3')
        great_day_1 = request.POST.get('great-day-1')
        great_day_2 = request.POST.get('great-day-2')
        great_day_3 = request.POST.get('great-day-3')
        affirmation = request.POST.get('affirmation')
        # Save the morning reflection, e.g., to the database or session
        request.session['morning_reflection'] = {
            'gratitude': [gratitude_1, gratitude_2, gratitude_3],
            'great_day': [great_day_1, great_day_2, great_day_3],
            'affirmation': affirmation,
        }
        return redirect('dashboard')

# Handle Evening Reflection
def evening_reflection(request):
    if request.method == 'POST':
        highlights_1 = request.POST.get('highlights-1')
        highlights_2 = request.POST.get('highlights-2')
        highlights_3 = request.POST.get('highlights-3')
        lesson_learned = request.POST.get('lesson-learned')
        # Save the evening reflection, e.g., to the database or session
        request.session['evening_reflection'] = {
            'highlights': [highlights_1, highlights_2, highlights_3],
            'lesson_learned': lesson_learned,
        }
        return redirect('dashboard')
    
def best_case_scenario(request):
    if request.method == 'POST':
        best_case = request.POST.get('best-case-scenario')
        # Save the best case scenario, e.g., to the database or session
        request.session['best_case_scenario'] = best_case
        return redirect('dashboard')