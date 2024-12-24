from django.urls import path
from . import views

urlpatterns = [
    path('RAG/', views.RAG, name='RAG'),  # RAG
]
