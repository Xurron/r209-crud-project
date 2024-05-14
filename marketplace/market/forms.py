from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class ItemForm(ModelForm):
    class Meta:
        model = models.Item
        fields = ['name', 'price', 'description', 'quantity']
        labels = {
            'name': _('Nom'),
            'price': _('Prix'),
            'description': _('Description'),
            'quantity': _('Quantité'),
        }
        error_messages = {
            'name': {
                'max_length': _("Le nom de l\'article est trop long."),
            },
        }

class UserForm(ModelForm):

    class Meta:
        model = models.User
        fields = ['name', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
        labels = {
            'name': _('Nom'),
            'email': _('Email'),
            'password': _('Mot de passe'),
        }
        error_messages = {
            'name': {
                'max_length': _("Le nom de l\'utilisateur est trop long."),
            },
        }