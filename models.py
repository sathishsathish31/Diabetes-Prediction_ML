from django.db import models

class Prediction(models.Model):
    pregnancy = models.IntegerField()
    glucose = models.FloatField()
    blood_pressure = models.FloatField()
    skin_thickness = models.FloatField()
    insulin = models.FloatField()
    bmi = models.FloatField()
    diabetic_function = models.FloatField()
    age = models.IntegerField()
    outcome = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)