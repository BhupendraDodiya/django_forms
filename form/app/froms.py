from django import forms
from .models import Friend

class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['name','age','dob','active','email','password']
        labels = {'name':'NAME','age':'AGE','dob':'DOB','active':'ACTIVE','email':'EMAIL',
                  'password':'PASSWORD'}
        widgets = {'name':forms.TextInput(attrs={'placeholder':'enter name'}),
                   'age':forms.TextInput(attrs={'placeholder':'enter age'}),
                   'dob':forms.TextInput(attrs={'placeholder':'enter dob'}),
                   'email':forms.EmailInput(attrs={'placeholder':'enter email'}),
                   'password':forms.PasswordInput(attrs={'placeholder':'enter password'}),
                   }