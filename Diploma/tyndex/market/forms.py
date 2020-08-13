from django.forms import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Article

from ckeditor.widgets import CKEditorWidget


class CustomerLoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control',
               'placeholder': 'Email адрес'}))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control',
               'placeholder': 'Пароль'}))

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            customer = User.objects.filter(email=email).first()

            if not customer:
                raise forms.ValidationError('Покупатель с таким адресом email не зарегистрирован')

            else:
                username = customer.username

                user = authenticate(username=username, password=password, )

                if not user:
                    raise forms.ValidationError('Неверный адрес email или пароль')

        return super().clean()


class CustomerRegisterForm(UserCreationForm):
    email = forms.CharField(
        label='Email адрес:',
        widget=forms.EmailInput(
            attrs={'class': 'form-control form-control-lg', 'placeholder': 'Введите ваш email'}
        )
    )

    password1 = forms.CharField(
        label='Пароль:',
        strip=False,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control form-control-lg', 'placeholder': 'Придумайте пароль'}
        )
    )
    password2 = forms.CharField(
        label='Повторите пароль:',
        strip=False,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control form-control-lg', 'placeholder': 'Введите пароль еще раз'}
        )
    )

    class Meta:
        model = User
        fields = ('email',)

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Пользователь с таким email уже зарегистрирован'
            )
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()
        return user
