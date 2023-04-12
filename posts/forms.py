from django import forms
from .models import Comments, PostsModel, Reply
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    title = forms.CharField(required=False, widget=forms.TextInput(attrs={"class":"form-control"}))
    content = forms.CharField(required=False, widget=forms.Textarea(attrs={"class":"r-5 form-control"}))
    class Meta:
        model = PostsModel
        fields = ['title', 'content', 'photo', 'category']
        widgets = {
                'category' : forms.Select(attrs={"class":"r-5 form-control"})
            }


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=100, label='Create username', help_text="Up to 100 characters. It may contain only letters, numbers and "
                     "@/./+/-/_ characters.", widget=forms.TextInput(attrs={"class":"form-control"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}), label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}), label='Repeat password')
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields=['content',]
        widgets={
            'content' : forms.TextInput(attrs={"class":"form-control"})
        }


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['content']
        widgets={
            'content' : forms.TextInput(attrs={"class":"form-control"})
        }

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100, label='Enter username', widget=forms.TextInput(attrs={"class":"form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}), label='Password')
    class Meta:
        model = User
        fields = ['username', 'password']