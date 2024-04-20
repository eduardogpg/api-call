import requests
from django.shortcuts import render
from django.shortcuts import redirect
from django.db import transaction

from .models import Userlog

def _get_courses():
    url = 'http://127.0.0.1:8001/api/v1/courses/'
    if (response := requests.get(url)).status_code == 200:
        return response.json()
    
    return None

def _update_course(pk):
    url = f'http://127.0.0.1:8001/api/v1/courses/{pk}/publish'
    response = requests.put(url)
    if response.status_code == 200:
        return response.json()
    
    raise Exception('Error updating course:', response.status_code)


def update_course(request, pk):
    try:
        with transaction.atomic():
            _update_course(pk)
            Userlog.objects.create(action=f'Course {pk} updated')

    except Exception as e:
        print(e)
        
    return redirect('home')

def home(request):
    response = _get_courses()
    return render(request, 'users/home.html', {
        'courses': response or []
    })
