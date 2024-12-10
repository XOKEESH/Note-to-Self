from django.urls import path
from . import views 

urlpatterns = [
   path('', views.home, name='home'),
   path('about/', views.about, name='about'),
   path('dashboard/', views.dashboard, name='dashboard'),
   path('settings/', views.settings, name='settings'),
   path('morning-reflection/', views.morning_reflection, name='morning_reflection'),
   path('evening-reflection/', views.evening_reflection, name='evening_reflection'),
   path('best-case-scenario/', views.best_case_scenario, name='best_case_scenario'),
]
