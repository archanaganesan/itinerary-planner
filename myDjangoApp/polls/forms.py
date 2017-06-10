from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class ItineraryForm(forms.Form):
    city = forms.CharField(max_length=60)
    state = forms.CharField(max_length=60)
    from_date = forms.DateField(widget=forms.SelectDateWidget)
    to_date = forms.DateField(widget=forms.SelectDateWidget)
