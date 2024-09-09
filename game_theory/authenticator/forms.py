from django import forms
from django.contrib.auth.models import User
from .models import GTUser
from panel.models import Group
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    group_id = forms.IntegerField(required=True)

    class Meta:
        model = GTUser
        fields = ('username', 'email', 'password1', 'password2', 'group_id')

    def clean_group_id(self):
        group_id = self.cleaned_data.get('group_id')
        try:
            group_instance = Group.objects.get(id=group_id)
        except Group.DoesNotExist:
            self.add_error('group_id', f'Group with id {group_id} does not exist!')
            return None
        return group_instance

        

class LoginForm(AuthenticationForm):
    class Meta:
        model = GTUser
        fields = ('username', 'password')
