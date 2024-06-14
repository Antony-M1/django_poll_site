"""
This file contains all the application functions
"""
from django.http import HttpResponse

# Create your views here.


def index(request) -> HttpResponse:
    """
        Polls Index Funtions
    """
    return HttpResponse("Hello, world. You're at the polls index.")
