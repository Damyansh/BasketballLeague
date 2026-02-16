import datetime

from django import forms

from common.models import Award


class AwardForm(forms.ModelForm):
    class Meta:
        model = Award
        fields = '__all__'

        labels = {
            'title': 'Award Title',
            'year': 'Year Awarded',
            'players': 'Players',
        }

        widgets = {
            'year': forms.Select(choices=[(year, year) for year in range(datetime.date.today().year, 1900, -1)]),
        }

class AwardUpdateForm(forms.ModelForm):
    class Meta:
        model = Award
        fields = ['title', 'year']