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