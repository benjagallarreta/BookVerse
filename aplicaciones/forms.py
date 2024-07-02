from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Usuario

class RegistroForm(UserCreationForm):
    domicilio = forms.CharField(max_length=250, required=False)
    nacionalidad = forms.CharField(max_length=80, required=False)
    nroTelefono = forms.CharField(max_length=80, required=False)
    correoElectronicoSecundario = forms.EmailField(max_length=250, required=False)
    birth_date = forms.DateField(required=False)

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'domicilio', 'nacionalidad', 'nroTelefono', 'correoElectronicoSecundario', 'birth_date', 'password1', 'password2')

def save(self, commit=True):
        user = Usuario(
            username=self.cleaned_data['username'],
            domicilio=self.cleaned_data['domicilio'],
            nacionalidad=self.cleaned_data['nacionalidad'],
            nroTelefono=self.cleaned_data['nroTelefono'],
            correoElectronicoSecundario=self.cleaned_data['correoElectronicoSecundario'],
            birth_date=self.cleaned_data['birth_date'],
        )
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de Usuario'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))