from django.urls import path
from .views import (
    home,
    MemberListView,
    MemberDetailView,
    ContributionListView,
    ContributionDetailView,
    search_results,
    login_view,
    register_view,
)

app_name = 'baduma_youths'

urlpatterns = [
    # Base pages
    path('', home, name='home'),

    # Member URLs
    path('members/', MemberListView.as_view(), name='member_list'),
    path('members/<int:pk>/', MemberDetailView.as_view(), name='member_detail'),

    # Contribution URLs
    path('contributions/', ContributionListView.as_view(), name='contribution_list'),
    path('contributions/<int:pk>/', ContributionDetailView.as_view(), name='contribution_detail'),

    # Auth & Search
    path('search/', search_results, name='search_results'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
]