"""
The urls for the super_tools app
"""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.WritingToolsAPIView.as_view(), name="writing-tools"),
]
