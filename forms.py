from django import forms

class PredictionForm(forms.Form):
    pregnancy = forms.IntegerField()
    glucose = forms.FloatField()
    blood_pressure = forms.FloatField()
    skin_thickness = forms.FloatField()
    insulin = forms.FloatField()
    bmi = forms.FloatField()
    diabetic_function = forms.FloatField()
    age = forms.IntegerField()