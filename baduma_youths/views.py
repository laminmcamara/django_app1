from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from .models import Member, Contribution
from .forms import CMSRegistrationForm, CMSLoginForm

# Home view
def home(request):
    members = Member.objects.all()  # Fetch all members
    context = {
        'members': members,
    }
    return render(request, 'baduma_youths/home.html', context)

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
class SearchView(ListView):
    template_name = 'baduma_youths/search_results.html'
    context_object_name = 'results'

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        members = Member.objects.filter(first_name__icontains=query) | \
                  Member.objects.filter(last_name__icontains=query)
        contributions = Contribution.objects.filter(description__icontains=query)
        return {
            'members': members,
            'contributions': contributions,
            'query': query,
        }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_queryset())
        return context

# Registration View
def register_view(request):
    if request.method == 'POST':
        form = CMSRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('home')  # Redirect to the home page after registration
    else:
        form = CMSRegistrationForm()
    return render(request, 'baduma_youths/register.html', {'form': form})

# Login View
def login_view(request):
    if request.method == 'POST':
        form = CMSLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to home after login
            else:
                form.add_error(None, "Invalid credentials")
    else:
        form = CMSLoginForm()
    return render(request, 'baduma_youths/login.html', {'form': form})

# Custom 404 error page
def custom_404(request, exception):
    return render(request, 'baduma_youths/404.html', status=404)