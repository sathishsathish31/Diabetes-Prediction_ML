import numpy as np
import pickle
from django.shortcuts import render
from .forms import PredictionForm

# Load model (once when the server starts)
with open("prediction/model/knn_model.pkl", "rb") as f:

    model = pickle.load(f)

def predict_diabetes(request):
    result = None
    if request.method == "POST":
        form = PredictionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            input_data = np.array([[
                data['pregnancy'],
                data['glucose'],
                data['blood_pressure'],
                data['skin_thickness'],
                data['insulin'],
                data['bmi'],
                data['diabetic_function'],
                data['age'],
            ]])
            prediction = model.predict(input_data)[0]
            result = "Sorry!  You Have a Diabetic 😔💯" if prediction == 1 else "Not Diabetic 🤩"
    else:
        form = PredictionForm()

    return render(request,"prediction/predict.html", {"form": form, "result": result})