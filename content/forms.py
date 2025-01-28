from django import forms

class RegisterForm(forms.Form):
    """
    A form for user registration with validation for passwords and phone numbers.
    """
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={"placeholder": "Enter your username"})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "Enter your email"})
    )
    phone_number = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={"placeholder": "Enter your phone number"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Enter your password"})
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Confirm your password"})
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data
