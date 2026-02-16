from django import forms

from players.models import Player



class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = '__all__'
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'position': 'Position',
            'team': 'Team',
            'points_per_game': 'Points Per Game',
            'rebounds_per_game': 'Rebounds Per Game',
            'assists_per_game': 'Assists Per Game',
            'photo': 'Player Photo',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter first name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter last name'}),
            'points_per_game': forms.NumberInput(attrs={'step':0.1,'min': 0}),
            'rebounds_per_game': forms.NumberInput(attrs={'step':0.1,'min': 0}),
            'assists_per_game': forms.NumberInput(attrs={'step':0.1,'min': 0}),
        }

        help_texts = {
            'position': 'Select players position on the court',
            'team': 'Choose the team this player belongs to',
        }



class PlayerDeleteForm(PlayerForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['disabled'] = True
            field.widget.attrs['readonly'] = True