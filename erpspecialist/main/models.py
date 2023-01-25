from django.db import models


# Create your models here.
class ByYearStatistic(models.Model):
    year = models.IntegerField('Год')
    salary_by_year = models.IntegerField('Динамика уровня зарплат по годам')
    count_by_year = models.IntegerField('Динамика количества вакансий по годам')
    vac_salary_by_year = models.IntegerField('Динамика уровня зарплат по годам для выбранной профессии')
    vac_count_by_year = models.IntegerField('Динамика количества вакансий по годам для выбранной профессии')


class ByCityStatistic(models.Model):
    city_salary = models.CharField('Город (для зарплат)', max_length=100)
    salary = models.IntegerField('Уровень зарплат по городам')
    city_part = models.CharField('Город (для доли вакансий)', max_length=100)
    part = models.DecimalField('Доля вакансий по городам', max_digits=4, decimal_places=4)


class SkillStatistic(models.Model):
    year = models.IntegerField('Год')
    skills = models.TextField('Топ-10 Навыков', max_length=250)


class Images(models.Model):
    year_salary = models.FileField('Динамика уровня зарплат по годам')
    year_count = models.FileField('Динамика количества вакансий по годам')
    city_salary = models.FileField('Динамика зарплат по городам')
    city_part = models.FileField('Доля ваканский по городам')
    year_skills = models.FileField('Топ-10 навыков по годам')
