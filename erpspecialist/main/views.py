from django.shortcuts import render
from .utils import get_data
import requests


def index(req):
    return render(req, 'main/index.html')


def demands(req):
    return render(req, 'main/demands.html')


def geography(req):
    return render(req, 'main/geography.html')


def skills(req):
    return render(req, 'main/skills.html')


def latest(req):
    payload = {
        'text': 'erp',
        'search_field': 'name',
        'order_by': 'publication_time',
        'only_with_salary': 'true'
    }
    data = get_data(requests.get('https://api.hh.ru/vacancies', params=payload))
    return render(req, 'main/latest.html', {'data': data})
