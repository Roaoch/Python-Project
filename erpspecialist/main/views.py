from django.shortcuts import render


def index(req):
    return render(req, 'main/index.html')


def demands(req):
    return render(req, 'main/demands.html')


def geography(req):
    return render(req, 'main/geography.html')


def skills(req):
    return render(req, 'main/skills.html')


def latest(req):
    return render(req, 'main/latest.html')