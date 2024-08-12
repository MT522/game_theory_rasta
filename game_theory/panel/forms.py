from django import forms
from .models import Group

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