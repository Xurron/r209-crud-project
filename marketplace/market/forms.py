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
        help_texts = {
            'name': _('Saisir le nom de l\'article'),
            'price': _('Saisir le prix de l\'article'),
            'description': _('Saisir la description de l\'article'),
            'quantity': _('Saisir la quantité de l\'article'),
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
        labels = {
            'name': _('Nom'),
            'email': _('Email'),
            'password': _('Mot de passe'),
        }
        help_texts = {
            'name': _('Saisir le nom de l\'utilisateur'),
            'email': _('Saisir l\'email de l\'utilisateur'),
            'password': _('Saisir le mot de passe de l\'utilisateur'),
        }
        error_messages = {
            'name': {
                'max_length': _("Le nom de l\'utilisateur est trop long."),
            },
        }