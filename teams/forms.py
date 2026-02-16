from django import forms

from teams.models import Team


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'
        labels = {
            'name': 'Team Name',
            'city': 'City',
            'year_founded': 'Year Founded',
            'coach_name': 'Head Coach',
            'logo': 'Team Logo',
        }

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter team name'}),
        'city': forms.TextInput(attrs={'placeholder': 'Enter city'}),
        'year_founded': forms.NumberInput(attrs={'placeholder': 'Enter year founded'}),
        'coach_name': forms.TextInput(attrs={'placeholder': 'Coach full name'}),
        }

        error_messages = {
            'name': {
                'unique': 'A team with this name already exists.',
                'required': 'Please enter a team name.',
            },
            'city': {
                'required': 'Please enter a city.',
        },
        }



class TeamDeleteForm(TeamForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['disabled'] = True
            field.widget.attrs['readonly'] = True