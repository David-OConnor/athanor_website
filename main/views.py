from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def home(request: HttpRequest) -> HttpResponse:
    """View for the home page"""
    return render(request, "index.html", {})


def downloads(request: HttpRequest) -> HttpResponse:
    return render(request, "downloads.html", {})

# def about(request: HttpRequest) -> HttpResponse:
#     return render(request, "about.html", {})


def privacy(request: HttpRequest) -> HttpResponse:
    return render(request, "privacy.html", {})


def terms(request: HttpRequest) -> HttpResponse:
    return render(request, "terms.html", {})