"""
The urls for the super_tools app
"""

from django.urls import path
from . import views

urlpatterns = [
    path("ai-text-summarizer/", views.AiTextSummarizerView.as_view(), name="ai-text-summarizer"),
]
