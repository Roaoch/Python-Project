from django.shortcuts import render
from .utils import get_data
from .models import ByYearStatistic, ByCityStatistic, SkillStatistic, Images
import requests


def index(req):
    return render(req, 'main/index.html')


def demands(req):
    data = ByYearStatistic.objects.all()
    images = Images.objects.get()
    return render(req, 'main/demands.html', {'data': data, 'images': images})


def geography(req):
    data = ByCityStatistic.objects.all()
    images = Images.objects.get()
    return render(req, 'main/geography.html', {'data': data, 'images': images})


def skills(req):
    data = SkillStatistic.objects.all()
    images = Images.objects.get()
    return render(req, 'main/skills.html', {'data': data, 'images': images})


def latest(req):
    payload = {
        'text': 'erp',
        'search_field': 'name',
        'order_by': 'publication_time',
        'only_with_salary': 'true'
    }
    data = get_data(requests.get('https://api.hh.ru/vacancies', params=payload))
    return render(req, 'main/latest.html', {'data': data})
