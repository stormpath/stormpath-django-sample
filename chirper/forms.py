from django import forms
from django.utils.safestring import mark_safe
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from django_stormpath.forms import (StormpathUserCreationForm,
        StormpathUserChangeForm)

from .models import Chirp, ChirperUser


class HorizontalRadioRenderer(forms.RadioSelect.renderer):
    def render(self):
        return mark_safe(u'\n'.join(u'%s\n' % w for w in self))


class ChirperCreateForm(StormpathUserCreationForm):
    pass


class ChirperUpdateForm(StormpathUserChangeForm):
    class Meta:
        model = ChirperUser
        exclude = ('user_permissions', 'last_login', 'password',
                'href', 'groups')

    def __init__(self, *args, **kwargs):
        super(ChirperUpdateForm, self).__init__(*args, **kwargs)
        self.fields['password'].help_text = 'Passwords are not stored in the local DB. <a href="/change/password/">Change password here</a>'
        self.fields['is_active'].widget.attrs['disabled'] = 'disabled'
        self.fields['is_admin'].widget.attrs['disabled'] = 'disabled'
        self.fields['is_staff'].widget.attrs['disabled'] = 'disabled'
        self.fields['is_superuser'].widget.attrs['disabled'] = 'disabled'


class ChirpForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
            super(ChirpForm, self).__init__(*args, **kwargs)
            self.fields['message'].widget.attrs['rows'] = 3
            self.fields['message'].widget.attrs['placeholder'] = \
                "Compose your chirp here..."

    class Meta:
        model = Chirp
        exclude = ("user", "owner_is_admin", "owner_is_premium")
