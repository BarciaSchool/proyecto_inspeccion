from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.utils.translation import gettext as _

class loginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    
class RegistroForm(UserCreationForm):
    email = forms.EmailField(label=_('Correo electrónico'))
    first_name = forms.CharField(max_length=100, label=_('Nombre'))
    last_name = forms.CharField(max_length=100, label=_('Apellido'))
    cedula = forms.CharField(max_length=10, label=_('Cédula'))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'cedula', 'password1', 'password2']
        labels = {
            'username': _('Nombre de usuario'),
            'password1': _('Contraseña'),
            'password2': _('Confirmar contraseña'),
        }

    def __init__(self, *args, **kwargs):
        super(RegistroForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Registrarse'))
