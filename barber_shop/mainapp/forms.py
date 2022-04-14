from django import forms
from django.contrib.auth.password_validation import CommonPasswordValidator, get_default_password_validators, \
    validate_password
from django.core.validators import MinLengthValidator, MaxLengthValidator


class LoginForm(forms.Form):
    login = forms.CharField(label='Логин', max_length=20,
                            widget=forms.TextInput(attrs={'class': 'login-field  login-form-field  form-field',
                                                          'placeholder': 'Логин'}),
                            validators=[
                                MinLengthValidator(limit_value=5, message="Логин должен содержать от 5 до 20 символов"),
                                MaxLengthValidator(limit_value=20,
                                                   message="Логин должен содержать от 5 до 20 символов"),
                            ])
    password = forms.CharField(label='Пароль', max_length=100,
                               widget=forms.PasswordInput(attrs={'class': 'password-field  login-form-field  form-field',
                                                             'placeholder': 'Пароль'}),
                               )


class RegistrationForm(forms.Form):
    login = forms.CharField(label='Логин', max_length=20,
                            widget=forms.TextInput(attrs={'class': 'login-field  login-form-field  form-field',
                                                          'placeholder': 'Логин'}),
                            validators=[
                                MinLengthValidator(limit_value=5, message="Логин должен содержать от 5 до 20 символов"),
                                MaxLengthValidator(limit_value=20,
                                                   message="Логин должен содержать от 5 до 20 символов"),
                            ])
    password = forms.CharField(label='Пароль', max_length=100,
                               widget=forms.PasswordInput(attrs={'class': 'password-field  login-form-field  form-field',
                                                             'placeholder': 'Пароль'}),
                               validators=[
                                   validate_password
                               ]
                               )
    reply_password = forms.CharField(label='Повтор пароля', max_length=100,
                                     widget=forms.PasswordInput(
                                         attrs={'class': 'password-field  login-form-field  form-field',
                                                'placeholder': 'Повторите пароль'}), )

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        reply_password = cleaned_data.get('reply_password')

        if password and reply_password:
            if password != reply_password:
                self.add_error('reply_password', 'Пароли не совпадают')
        return cleaned_data
