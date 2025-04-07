from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Member, Contribution

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
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class ContributionForm(forms.ModelForm):
    class Meta:
        model = Contribution
        fields = ['member', 'contribution_type', 'amount', 'description']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if self.user and self.user.is_authenticated:
            self.fields['member'].queryset = Member.objects.filter(user=self.user)
            self.fields['member'].initial = self.user.member
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class CMSRegistrationForm(UserCreationForm):
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
        fields = ('username', 'email', 'password1', 'password2', 'phone_number', 'gender')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
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
        
        try:
            user = User.objects.get(email=email)
            if not user.check_password(password):
                raise forms.ValidationError("Invalid credentials")
        except User.DoesNotExist:
            raise forms.ValidationError("User with this email does not exist")
            
        return cleaned_data