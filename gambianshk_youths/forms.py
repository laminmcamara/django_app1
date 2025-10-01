# gambianshk_youths/forms.py

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Member, Contribution, Constitution, Attendance, Meeting
from django_ckeditor_5.widgets import CKEditor5Widget

User = get_user_model()

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = [
            'first_name', 'last_name', 'email', 
            'phone_number', 'profile_picture', 'career',
            'educational_background', 'age', 'marital_status', 'gender'
        ]
        widgets = {
            'educational_background': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.setdefault('class', 'form-control')


class ContributionForm(forms.ModelForm):
    class Meta:
        model = Contribution
        fields = ['member', 'contribution_type', 'amount', 'description']  
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if self.user and self.user.is_authenticated:
            self.fields['member'].queryset = Member.objects.filter(user=self.user)  # Adjust queryset for member
            try:
                self.fields['member'].initial = self.user.member.id  # Update to use member ID
            except Member.DoesNotExist:
                pass
        for field in self.fields:
            self.fields[field].widget.attrs.setdefault('class', 'form-control')


class CMSRegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    phone_number = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    gender = forms.ChoiceField(
        choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'phone_number', 'gender')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']  # Save first name
        user.last_name = self.cleaned_data['last_name']    # Save last name
        if commit:
            user.save()
            Member.objects.create(
                user=user,
                phone_number=self.cleaned_data['phone_number'],
                gender=self.cleaned_data['gender']
            )
        return user


class CMSLoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        
        if email and password:
            try:
                user = User.objects.get(email=email)
                if not user.check_password(password):
                    raise forms.ValidationError("Invalid credentials")
            except User.DoesNotExist:
                raise forms.ValidationError("User with this email does not exist")
        return cleaned_data


class ConstitutionForm(forms.ModelForm):
    class Meta:
        model = Constitution
        fields = ['title', 'content', 'effective_date']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'effective_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.setdefault('class', 'form-control')


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['meeting', 'member']  
        widgets = {
            'meeting': forms.Select(attrs={'class': 'form-control'}),
            'member': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.setdefault('class', 'form-control')

class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ['title', 'date', 'agenda', 'minutes']  # Add or adjust fields as necessary
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'agenda': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'minutes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.setdefault('class', 'form-control')

class PostForm(forms.Form):
    content = forms.CharField(widget=CKEditor5Widget())