from django import forms
from django_stormpath.forms import UserCreateForm
from stormpath.client import Client
from django.utils.safestring import mark_safe
from django.conf import settings
from .models import Chirp


class HorizontalRadioRenderer(forms.RadioSelect.renderer):
    def render(self):
        return mark_safe(u'\n'.join(u'%s\n' % w for w in self))


class ChirperCreateForm(UserCreateForm):

    ACC_CHOICES = (
        ('Admins', 'Administrator',),
        ('Premiums', 'Premium',),
        ('Basics', 'Basic'))

    account_type = forms.ChoiceField(
        widget=forms.RadioSelect(renderer=HorizontalRadioRenderer),
        choices=ACC_CHOICES,
        initial='Basics')

    def save(self):
        super(ChirperCreateForm, self).save()
        client = Client(api_key={'id': settings.STORMPATH_ID,
                'secret': settings.STORMPATH_SECRET})
        account_type = self.cleaned_data['account_type']
        if account_type == 'Admins':
            admin_group = client.groups.get(
                settings.STORMPATH_ADMINISTRATORS)
            self.account.add_group(admin_group)
            self.account.save()

        elif account_type == 'Premiums':
            premium_group = client.groups.get(settings.STORMPATH_PREMIUMS)
            self.account.add_group(premium_group)
            self.account.save()


class ChirpForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
            super(ChirpForm, self).__init__(*args, **kwargs)
            self.fields['message'].widget.attrs['rows'] = 3
            self.fields['message'].widget.attrs['placeholder'] = \
                "Compose your chirp here..."

    class Meta:
        model = Chirp
        exclude = ("user", "owner_is_admin", "owner_is_premium")
