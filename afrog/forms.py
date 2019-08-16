from django import forms
from .models import UserProfile
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from django.forms import ModelForm



# class CommentForm(forms.ModelForm):

#     class Meta:
#         model = Comments
#         exclude = ['poster', 'date_posted']



# class NewProjectForm(forms.ModelForm):
#     class Meta:
#         model = Project
#         exclude = ['poster', 'pub_date']




class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('bio', 'phone', 'pic')
        # exclude = ['user','pub_date']