from django import forms

from games.models import Game, GamePlayerStats


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['date', 'home_team', 'away_team', 'home_score', 'away_score']
        labels = {
            'date': 'Game Date',
            'home_team': 'Home Team',
            'away_team': 'Away Team',
            'home_score': 'Home Team Score',
            'away_score': 'Away Team Score',
        }
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'home_score': forms.NumberInput(attrs={'min': 0}),
            'away_score': forms.NumberInput(attrs={'min': 0}),
        }


class GamePlayerStatsForm(forms.ModelForm):
    class Meta:
        model = GamePlayerStats
        fields = ['player', 'points', 'rebounds', 'assists']



        widgets ={
            'points': forms.NumberInput(attrs={'min': 0}),
            'rebounds': forms.NumberInput(attrs={'min': 0}),
            'assists': forms.NumberInput(attrs={'min': 0}),
        }


class GameDeleteForm(GameForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['disabled'] = True
            field.widget.attrs['readonly'] = True