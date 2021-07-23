from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model

User = get_user_model()

class SignUpForm(forms.ModelForm):
    username = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Имя пользователя',
    }))
    password = forms.CharField(min_length=6, max_length=255, required=True, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Пароль',
    }))
    password2 = forms.CharField(min_length=6, max_length=255, required=True, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Повторите пароль',
    }))

    def clean(self):
        if not self.cleaned_data['password'] == self.cleaned_data['password2'] or not self.cleaned_data['password2']:
            self._errors['password2'] = self.error_class(['Пароли не совпадают'])
        return self.cleaned_data

    def save(self, commit=True):
        user = User( 
                username=self.cleaned_data['username'], password=make_password(self.cleaned_data['password'], None, 'md5')
                )
        return user.save()

    class Meta:
        model = User
        fields = ('username', 'password', 'password2')


class LogInForm(forms.ModelForm):

    username = forms.EmailField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'username',
    }))

    password = forms.CharField(min_length=6, max_length=255, required=True, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Пароль',
    }))

    class Meta:
        model = User
        fields = ('username', 'password')
