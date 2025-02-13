from django import forms
from django.core.exceptions import ValidationError
from .models import User,Feed_post

class RegisterForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label="Email",
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email", 'class': 'form-control'}),
    )
    phone_number = forms.CharField(  # Use CharField for phone numbers to avoid integer formatting issues
        max_length=15,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    confirm_password = forms.CharField(
        label="Confirm Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        phone_number = cleaned_data.get("phone_number")
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        # Validate username uniqueness
        if User.objects.filter(username=username).exists():
            raise ValidationError(username+" "+ "Username already exists.")
    
        # Validate email uniqueness
        if User.objects.filter(email=email).exists():
            raise ValidationError(email+" "+ "Email already exists.")

        # Validate phone number uniqueness
        if User.objects.filter(phone_number=phone_number).exists():
            raise ValidationError(phone_number+" "+ "Phone number already exists.")

        # Password validation
        if password:
            if len(password) < 8:
                self.add_error("Password must be at least 8 characters long.")
            if password != confirm_password:
                self.add_error("Passwords do not match.")

        return cleaned_data

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError(username+" "+ "Username does not exist")
        return cleaned_data
    
class FeedPostForm(forms.ModelForm):
    class Meta:
        model = Feed_post
        fields = ['title', 'content']
