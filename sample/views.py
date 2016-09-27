"""
Django views for the Chirper app.

Note that every save call either passes or raises an Exception.
This is because we want to print the messages provided by Stormpath.
"""


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.conf import settings

from django_stormpath.models import APPLICATION
from django_stormpath.forms import StormpathUserCreationForm
from django_stormpath.views import stormpath_id_site_callback
from stormpath.error import Error as StormpathError

from sample.forms import SampleUserCustomInfoForm


def handled_stormpath_id_site_callback(request):
    """Handle stormpath_id_site_callback's errors."""
    try:
        return stormpath_id_site_callback(request)
    except StormpathError:
        return redirect('sample:home')


def stormpath_login(request):
    """
    Verify user login.  It uses django_stormpath to check if user credentials
    are valid.
    """
    if settings.USE_ID_SITE:
        return redirect('sample:stormpath_id_site_login')

    if request.user.is_authenticated():
        return redirect('sample:home')

    form = AuthenticationForm(data=(request.POST or None))

    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('sample:home')
    print form.errors
    return render(
        request, 'login.html', {"form": form, 'id_site': settings.USE_ID_SITE})


@login_required
def stormpath_logout(request):
    """Simple logout view."""
    if settings.USE_ID_SITE:
        return redirect('sample:stormpath_id_site_logout')

    logout(request)
    return redirect('sample:home')


def register(request):
    """User creation view."""
    if settings.USE_ID_SITE:
        return redirect('sample:stormpath_id_site_register')

    form = StormpathUserCreationForm(request.POST or None)

    if form.is_valid():
        try:
            form.save()
            user = authenticate(
                username=request.POST['username'],
                password=request.POST['password1'])
            login(request, user)
            return redirect('sample:dashboard')
        except Exception as e:
            messages.add_message(request, messages.ERROR, str(e))
    return render(request, 'register.html', {"form": form})


@login_required
def dashboard(request):
    """
    This view renders a simple dashboard page for logged in users.

    Users can see their personal information on this page, as well as store
    additional data to their account (if they so choose).
    """
    form_data = request.POST.copy()
    form_data['user'] = request.user
    a = APPLICATION.accounts.get(request.user.href)
    if request.method == 'GET':
        form_data['birthday'] = a.custom_data.get('birthday')
        form_data['color'] = a.custom_data.get('color')

    form = SampleUserCustomInfoForm(form_data)

    if form.is_valid():
        form.save()

    return render(
        request, 'dashboard.html',
        {
            'birthday': a.custom_data.get('birthday'),
            'color': a.custom_data.get('color'),
            'form': form
        })
