from django import forms


class StudentForm(forms.Form):
    CHOICES = (
        ('1', 'Русский язык'),
        ('2', 'Математика'),
        ('3', 'Английский'),
        ('4', 'География')
    )
    name = forms.CharField(max_length=40)
    surname = forms.CharField(max_length=40)
    object = forms.ChoiceField(choices=CHOICES)

    average_score = forms.IntegerField()

class ObjectForm(forms.Form):
    name = forms.CharField(max_length=40)