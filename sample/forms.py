from django import forms
from django_stormpath.models import StormpathUser, APPLICATION

#
class SampleUserCustomInfoForm(forms.Form):
    user = forms.ModelChoiceField(
        queryset=StormpathUser.objects.all(), widget=forms.HiddenInput())
    birthday = forms.DateField(input_formats=('%m/%d/%Y',), required=False)
    color = forms.CharField(max_length=100, required=False)

    def save(self):
        cd = self.cleaned_data
        user, birthday, color = \
            cd.get('user'), cd.get('birthday'), cd.get('color')
        a = APPLICATION.accounts.get(user.href)
        if birthday:
            a.custom_data['birthday'] = birthday.strftime('%m/%d/%Y')
        elif 'birthday' in a.custom_data:
            a.custom_data['birthday'] = ''
        if color:
            a.custom_data['color'] = color
        elif 'color' in a.custom_data:
            a.custom_data['color'] = ''
        a.custom_data.save()
