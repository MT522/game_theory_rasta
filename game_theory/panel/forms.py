from django import forms
from .models import Group
from authenticator.models import GTUser

class AddScoreForm(forms.ModelForm):
    id = forms.IntegerField(max_value=10000)
    score = forms.IntegerField(max_value=10000)

    class Meta:
        model = Group
        fields = ('id', 'score')

    def clean(self):
        id = self.cleaned_data['id']
        
        groups = Group.objects.all()

        found = False
        for group in groups:
            if group.id == id:
                found = True
                break

        if found == False:
            self.add_error('id', 'Group with such ID does not exist!')

class AddNumberForm(forms.ModelForm):
    id = forms.IntegerField(max_value=10000)
    number1 = forms.FloatField(min_value=0.0, max_value=100.00, required=False)
    number2 = forms.FloatField(min_value=0.0, max_value=100.00, required=False)
    number3 = forms.FloatField(min_value=0.0, max_value=100.00, required=False)

    class Meta:
        model = Group
        fields = ('id', 'number1', 'number2', 'number3')
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(AddNumberForm, self).__init__(*args, **kwargs)

    def clean(self):
        id = self.cleaned_data['id']
        user = self.request.user
        gtuser = GTUser.objects.get(id=user.id)
        
        groups = Group.objects.all()

        found = False
        for group in groups:
            if group.id == id:
                found = True
                break

        if found == False:
            self.add_error('id', 'Group with such ID does not exist!')
            
        if gtuser == None:
            self.add_error('id', 'You are not a member of any group!')

        if gtuser.group_id.id != id:
            self.add_error('id', f'You are not authorized to submit numbers for this group!')

        if group.number1 != None or group.number2 != None or group.number3 != None:
            self.add_error('id', 'Group with such ID has already submitted its response!')
