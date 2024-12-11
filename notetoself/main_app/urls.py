from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('settings/', views.settings, name='settings'),
    path('morning-reflection/', views.morning_reflection, name='morning_reflection'),  # Renders the Morning Reflection template
    path('evening-reflection/', views.evening_reflection, name='evening_reflection'),  # Renders the Evening Reflection template
    path('best-case-scenario/', views.best_case_scenario, name='best_case_scenario'),  # Renders Best Case Scenario template
    # For form submissions (optional):
    path('morning-reflection/submit/', views.create_or_update_morning_reflection, name='submit_morning_reflection'),
    path('evening-reflection/submit/', views.create_or_update_evening_reflection, name='submit_evening_reflection'),
    path('best-case-scenario/submit/', views.create_or_update_best_case_scenario, name='submit_best_case_scenario'),
]

