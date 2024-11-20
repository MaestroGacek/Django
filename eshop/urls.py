from tkinter.font import names

from django.urls import path
from . import views

urlpatterns = [
    path(' ', views.index, name='index'),

    path('nabidka', views.nabidka, name='nabidka')
]