from django.urls import path
from . import views
import re

app_name = 'polls'

urlpatterns = [
    path('', views.show_polls, name='show_polls'),
    path('<int:pk>', views.detail_poll, name = 'detail_poll'),
    path('<int:pk>/vote', views.vote, name = 'vote'),
    path('<int:pk>/results', views.results, name='results')
    ]