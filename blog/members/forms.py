from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from blog.models import Profile

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=('username','email','password1','password2')

class UserUpdateDataForm(UserChangeForm):
    username = forms.CharField(label='Login' ,widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(label='Imie',required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Nazwisko',required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password')

class UserUpdateForm(forms.ModelForm):
    bio=forms.CharField(label='O mnie',required=False, widget=forms.Textarea(attrs={'class':'form-control'}))
    profile_pic=forms.ImageField(label='Zdjecie profilowe',required=False)
    facebook_url=forms.CharField(label='Facebook',required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    twitter_url=forms.CharField(label='Twitter',required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    instagram_url=forms.CharField(label='Instagram',required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model=Profile
        fields=['bio','facebook_url','twitter_url','instagram_url','profile_pic']

class UserCreateProfilePageForm(forms.ModelForm):
    user=forms.TextInput(attrs={'class':'form-control'})
    bio=forms.CharField(label='O mnie',required=False, widget=forms.Textarea(attrs={'class':'form-control'}))
    profile_pic=forms.ImageField(label='Zdjecie profilowe',required=False)
    facebook_url=forms.CharField(label='Facebook',required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    twitter_url=forms.CharField(label='Twitter',required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    instagram_url=forms.CharField(label='Instagram',required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model=Profile
        fields=['bio','facebook_url','twitter_url','instagram_url','profile_pic']