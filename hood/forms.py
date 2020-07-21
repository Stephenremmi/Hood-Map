from django import forms
from .models import Neighbourhood, Post,Business,Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
# from user.models import Profile

class CommunityModelForm(forms.ModelForm):
    
    class Meta:
        model = Neighbourhood
        fields = [ 'name','location']

class PostModelForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = [ 'description','categories','post_image']



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_path','community']


class CommunityModelForm(forms.ModelForm):
    
    class Meta:
        model = Neighbourhood
        fields = [ 'name','location','police','police_dpt_address','health_dpt','health_dpt_address']

class BusinessModelForm(forms.ModelForm):
    
    class Meta:
        model = Business
        fields = [ 'bsn_name','bsn_email']

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ['comment']