# gambianshk_youths/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.views import View

from django.views.generic import DetailView
from django.views.generic import ListView
from .models import Meeting, Attendance, Member, Contribution, Project, Event
from .forms import MeetingForm, AttendanceForm, CMSRegistrationForm  # TODO: Create these forms

# --- Existing Views (Correct) ---

ALLOWED_EXTENSIONS = {'mp4', 'mp3', 'wav', 'ogg', 'mov', 'jpg', 'jpeg', 'png', 'gif'}

class MediaUploadView(View):
    def post(self, request):
        uploaded_file = request.FILES.get('file')
        if uploaded_file:
            file_extension = uploaded_file.name.split('.')[-1].lower()
            if file_extension not in ALLOWED_EXTENSIONS:
                return JsonResponse({'error': 'Invalid file type'}, status=400)

            fs = FileSystemStorage()
            filename = fs.save(uploaded_file.name, uploaded_file)
            file_url = fs.url(filename)
            return JsonResponse({'url': file_url}, status=201)
        return JsonResponse({'error': 'No file uploaded'}, status=400)

# In your urls.py
from django.urls import path
from .views import MediaUploadView

urlpatterns = [
    path('upload/media/', MediaUploadView.as_view(), name='media-upload'),
]


def gambianshk_home(request):
    """Renders the home page."""
    return render(request, 'gambianshk_youths/home.html') 

def meeting_list(request):
    """Display a list of meetings."""
    meetings = Meeting.objects.all()
    return render(request, 'gambianshk_youths/meeting_list.html', {'meetings': meetings})

def meeting_detail(request, meeting_id):
    """Display details of a specific meeting."""
    meeting = get_object_or_404(Meeting, id=meeting_id)
    attendances = Attendance.objects.filter(meeting=meeting)
    return render(request, 'gambianshk_youths/meeting_detail.html', {
        'meeting': meeting,
        'attendances': attendances,
    })

def create_meeting(request):
    """Create a new meeting."""
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gambianshk_youths:meeting_list')
    else:
        form = MeetingForm()
    return render(request, 'gambianshk_youths/create_meeting.html', {'form': form})

def update_meeting(request, meeting_id):
    """Update an existing meeting."""
    meeting = get_object_or_404(Meeting, id=meeting_id)
    if request.method == 'POST':
        form = MeetingForm(request.POST, instance=meeting)
        if form.is_valid():
            form.save()
            return redirect('gambianshk_youths:meeting_detail', meeting_id=meeting.id)
    else:
        form = MeetingForm(instance=meeting)
    return render(request, 'gambianshk_youths/update_meeting.html', {'form': form})

def delete_meeting(request, meeting_id):
    """Delete a meeting."""
    meeting = get_object_or_404(Meeting, id=meeting_id)
    if request.method == 'POST':
        meeting.delete()
        return redirect('gambianshk_youths:meeting_list')
    return render(request, 'gambianshk_youths/delete_meeting.html', {'meeting': meeting})

def mark_attendance(request, meeting_id):
    """Mark attendance for a meeting."""
    meeting = get_object_or_404(Meeting, id=meeting_id)
    members = Member.objects.all()
    
    if request.method == 'POST':
        for member in members:
            attended = request.POST.get(f'attendance_{member.id}', 'off') == 'on'
            Attendance.objects.update_or_create(meeting=meeting, member=member, defaults={'attended': attended})
        return redirect('gambianshk_youths:meeting_detail', meeting_id=meeting.id)
    
    return render(request, 'gambianshk_youths/mark_attendance.html', {
        'meeting': meeting,
        'members': members,
    })
    
def member_list_view(request):
    """Displays a list of all members."""
    members = Member.objects.all()
    return render(request, 'gambianshk_youths/member_list.html', {'members': members})


# --- NEWLY ADDED VIEWS ---

def contribution_list_view(request):
    """Displays a list of all contributions."""
    # TODO: Fetch actual Contribution objects once your model is ready
    contributions = Contribution.objects.all()
    return render(request, 'gambianshk_youths/contribution_list.html', {'contributions': contributions})

def projects_list_view(request):
    """Displays a list of all projects."""
    # TODO: Fetch actual Project objects once your model is ready
    projects = Project.objects.all()
    return render(request, 'gambianshk_youths/projects_list.html', {'projects': projects})

def constitution_view(request):
    """Renders the constitution page. Content is likely handled by CMS."""
    return render(request, 'gambianshk_youths/constitution.html')

def search_view(request):
    """Renders the search results page. Logic might be handled by CMS or another app."""
    return render(request, 'gambianshk_youths/search_results.html')

def register_view(request):
    """Handles user registration."""
    if request.method == 'POST':
        form = CMSRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            return redirect('gambianshk_youths:gambianshk_home')
    else:
        form = CMSRegistrationForm()
    
    return render(request, 'gambianshk_youths/register.html', {'form': form})

def login_view(request):
    """Handles user login."""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('gambianshk_youths:gambianshk_home')
    else:
        form = AuthenticationForm()
    return render(request, 'gambianshk_youths/login.html', {'form': form})

def logout_view(request):
    """Handles user logout."""
    logout(request)
    return redirect('gambianshk_youths:baduma_home')

class EventDetailView(DetailView):
    model = Event
    template_name = 'gambianshk_youths/event_detail_plugin.html'
    context_object_name = 'event'

    def get_object(self, queryset=None):
        # Override to use slug field instead of primary key
        slug = self.kwargs.get('slug')
        return get_object_or_404(Event, slug=slug)  # Use get_object_or_404 for better error handling
    
def community_view(request):
    """Renders the community page. Content is likely handled by CMS."""
    return render(request, 'gambianshk_youths/community.html')



def news_view(request):
    return render(request, 'gambianshk_youths/news.html')

def terms_and_conditions_view(request):
    return render(request, 'gambianshk_youths/terms_and_conditions.html')