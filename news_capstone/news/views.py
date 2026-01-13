"""
Views for the News application.

This module contains view logic for handling HTTP requests
related to news articles and user interactions.
"""

from django.http import HttpResponse


def home(request):
    return HttpResponse("News Capstone is running ✅")
