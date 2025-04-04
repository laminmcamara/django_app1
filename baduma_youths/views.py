from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from .models import Member, Contribution

# Home view
def home(request):
    return render(request, 'baduma_youths/home.html')

# Member Views
class MemberListView(ListView):
    model = Member
    template_name = 'baduma_youths/member_list.html'
    context_object_name = 'members'

class MemberDetailView(DetailView):
    model = Member
    template_name = 'baduma_youths/member_detail.html'
    context_object_name = 'member'

# Contribution Views
class ContributionListView(ListView):
    model = Contribution
    template_name = 'baduma_youths/contribution_list.html'
    context_object_name = 'contributions'

class ContributionDetailView(DetailView):
    model = Contribution
    template_name = 'baduma_youths/contribution_detail.html'
    context_object_name = 'contribution'

# Search Results View
def search_results(request):
    query = request.GET.get('q')
    members = Member.objects.filter(name__icontains=query)
    contributions = Contribution.objects.filter(title__icontains=query)
    context = {
        'members': members,
        'contributions': contributions,
    }
    return render(request, 'baduma_youths/search_results.html', context)

# Login View
def login_view(request):
    return render(request, 'baduma_youths/login.html')

# Register View
def register_view(request):
    return render(request, 'baduma_youths/register.html')

def custom_404(request, exception):
    """Custom 404 error page."""
    return render(request, 'baduma_youths/404.html', status=404)