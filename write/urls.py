from django.urls import path
from . import views
import re

app_name = 'feedback'

urlpatterns = [
    path('', views.feedback, name = 'feedback')
]