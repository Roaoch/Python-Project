from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('demands', views.demands, name='demands'),
    path('geography', views.geography, name='geography'),
    path('skills', views.skills, name='skills'),
    path('latest', views.latest, name='latest')
]