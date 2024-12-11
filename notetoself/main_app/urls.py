from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('settings/', views.settings, name='settings'),
    path('accounts/signup/', views.signup, name='signup'),
    path('morning-reflection/', views.morning_reflection, name='morning_reflection'),  
    path('evening-reflection/', views.evening_reflection, name='evening_reflection'),
    path('best-case-scenario/', views.best_case_scenario, name='best_case_scenario'),
    path('morning-reflection/submit/', views.create_or_update_morning_reflection, name='submit_morning_reflection'),
    path('evening-reflection/submit/', views.create_or_update_evening_reflection, name='submit_evening_reflection'),
    path('best-case-scenario/submit/', views.create_or_update_best_case_scenario, name='submit_best_case_scenario'),
]

