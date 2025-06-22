from django.urls import path
from .import views

urlpatterns = [
    path('/prediction', views.predict_diabetes, name='predict'),
]