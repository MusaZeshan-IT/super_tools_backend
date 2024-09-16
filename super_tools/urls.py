"""
The urls for the super_tools app
"""

from django.urls import path
from . import views

urlpatterns = [
    path("summarize/", views.SummarizeTextView.as_view(), name="summarize-text"),
]
