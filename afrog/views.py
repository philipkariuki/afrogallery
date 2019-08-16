from django.shortcuts import render, redirect
from .models import *  # Project, UserProfile, Comments //
from .forms import *   # CommentForm, NewProjectForm, UserForm,  ProfileForm //
from django.http  import HttpResponse, Http404, HttpResponseRedirect
from registration.backends.simple.views import RegistrationView
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.db import transaction
from django.contrib import messages
from django.utils.translation import gettext as _

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    return render(request, 'index.html')


def profile(request):
	try:
		argz = { 'user' : request.user }
	except ObjectDoesNotExist:
		raise Http404()
	return render(request,'profile.html', {'profile':argz} )


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.userprofile)
    return render(request, 'profile_update.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

