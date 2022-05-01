from xml.etree.ElementInclude import include
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import  Comment, Employer,Post, Profile,Job, Jobseeker


class PaymentForm(forms.ModelForm):
    id = forms.IntegerField()
    name = forms.CharField()
    amount=forms.IntegerField(required=True)
    contact= forms.IntegerField(required=True)


class SignupForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.CharField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email')


class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['Full_name','Profile_image','address']
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = ['name']

class JobseekerForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username',  'email', 'password']

    
    def save(self):
        user = super().save(commit=False)
        user.is_jobseeker = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        jobseeker = Jobseeker.objects.create(user=user)
        jobseeker.email = self.cleaned_data.get('email')
        jobseeker.save()

        return jobseeker

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ('id', 'Title','Requirements','Location', 'Job Type')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['user']