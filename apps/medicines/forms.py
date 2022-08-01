from secrets import choice
from django import forms

from .models import Medicine


class MedicineEditForm(forms.ModelForm):
    medicine_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        ))
    dosage = forms.CharField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'id': 'dosage',
                'aria-describedby': 'dosage'
            }
        ))

    dosage_unit = forms.ChoiceField(
        choices=(
            ('Drop', 'Drop'),
            ('Pill', 'Pill'),
            ('Tablet', 'Tablet'),
            ('Vial', 'Vial'),
            ('Others', 'Others'),
        ),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'dosage',
                'aria-describedby': 'dosage'
            }
        ))
    frequency = forms.ChoiceField(
        choices=(('Daily', 'Daily'),
                 ('Weekly', 'Weekly'),
                 ('Monthly', 'Monthly'),),

        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'dosage',
                'aria-describedby': 'dosage'
            }
        ))
    frequency_unit = forms.ChoiceField(
        choices=(('Once', 'Once'),
                 ('Twice', 'Twice'),
                 ('Trice', 'Trice'),
                 ('Others', 'Others'),),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'dosage',
                'aria-describedby': 'dosage'
            }
        ))

    class Meta:
        model = Medicine
        exclude = ['user', 'created_at']
