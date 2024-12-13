from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('settings/', views.settings, name='settings'),
    path('accounts/signup/', views.signup, name='signup'),
    path('journal_entries/', views.JournalEntry_index, name='Journal_Entry_index'),
    
    path('journal_entries/<int:journal_entries_id>/', views.JournalEntry_detail, name='Journal_Entry_detail'),
    path('journal_entries/create/', views.JournalEntryCreate.as_view(), name='Journal_Entry_Create'),
    
    path('morningreflection/<int:morningref_id>/', views.MorningReflection_detail, name='Morning_Reflection_detail'),
    path('morningreflection/create/', views.MorningReflectionCreate.as_view(), name='Morning_Reflection_Create'),
    path('morningreflection/<int:pk>/update/', views.MorningReflectionUpdate.as_view(), name='Morning_Reflection_Update'),
    path('morningreflection/<int:pk>/delete/', views.MorningReflectionDelete.as_view(), name='Morning_Reflection_Delete'),
    
    path('eveningreflection/<int:eveningref_id>/', views.EveningReflection_detail, name='Evening_Reflection_detail'),
    path('eveningreflection/create/', views.EveningReflectionCreate.as_view(), name='Evening_Reflection_Create'),
    path('eveningreflection/<int:pk>/update/', views.EveningReflectionUpdate.as_view(), name='Evening_Reflection_Update'),
    path('eveningreflection/<int:pk>/delete/', views.EveningReflectionDelete.as_view(), name='Evening_Reflection_Delete'),
    
    path('bestcasescenario/<int:bestcase_id>/', views.BestCaseScenario_detail, name='Bestcase_Scenario_detail'),
    path('bestcasescenario/create/', views.BestCaseScenarioCreate.as_view(), name='Bestcase_Scenario_Create'),
    path('bestcasescenario/<int:pk>/update/', views.BestCaseScenarioUpdate.as_view(), name='Bestcase_Scenario_Update'),
    path('bestcasescenario/<int:pk>/delete/', views.BestCaseScenarioDelete.as_view(), name='Bestcase_Scenario_Delete'),
    ]
    