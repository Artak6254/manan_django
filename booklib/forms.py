from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    age = forms.IntegerField()
    school = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "age",
            "school",
            "password1",
            "password2",
        ]

    def save(self, commit=True):
        user = super().save(commit)
        Profile.objects.create(
            user=user,
            age=self.cleaned_data["age"],
            school=self.cleaned_data["school"],
        )
        return user
