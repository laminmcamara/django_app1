from django.urls import path
from . import views 

app_name = 'gambianshk_youths'

urlpatterns = [
    # Home page handled by CMS
    path('', views.gambianshk_home, name='gambianshk_home'),
    
    # Member and Contribution views
    path('members/', views.member_list_view, name='member'), 
    path('contributions/', views.contribution_list_view, name='contribution_list'),

    # Project view
    path('projects/', views.projects_list_view, name='projects_list'),

    # Constitution view handled by CMS
    path('constitution/', views.constitution_view, name='constitution'),

    # Search results handled by CMS
    path('search_results/', views.search_view, name='search_results'),

    # Authentication views
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Event view handled by CMS
    # path('events/', views.events_view, name='events'),
    path('event/<slug:slug>/', views.EventDetailView.as_view(), name='events'),

    # Community view handled by CMS
    path('community/', views.community_view, name='community'),

    # Meeting URLs 
    path('meetings/', views.meeting_list, name='meeting_list'),
    path('meetings/<int:meeting_id>/', views.meeting_detail, name='meeting_detail'),
    path('meetings/create/', views.create_meeting, name='create_meeting'),
    path('meetings/update/<int:meeting_id>/', views.update_meeting, name='update_meeting'),
    path('meetings/delete/<int:meeting_id>/', views.delete_meeting, name='delete_meeting'),
    path('meetings/<int:meeting_id>/mark-attendance/', views.mark_attendance, name='mark_attendance'),
    
    # Media upload endpoint
    path('upload/media/', views.MediaUploadView.as_view(), name='media-upload'),  

    # News view
    path('news/', views.news_view, name='news'),  # Ensure views.news_view is imported
    path('terms-and-conditions/', views.terms_and_conditions_view, name='terms_and_conditions'),

]