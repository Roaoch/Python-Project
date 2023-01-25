# Generated bycitystatistic Django 4.1.5 on 2023-01-22 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ByYearStatistic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(verbose_name='Год')),
                ('salary_by_year', models.IntegerField(verbose_name='Динамика уровня зарплат по годам')),
                ('count_by_year', models.IntegerField(verbose_name='Динамика количества вакансий по годам')),
                ('vac_salary_by_year', models.IntegerField(verbose_name='Динамика уровня зарплат по годам для выбранной профессии')),
                ('vac_count_by_year', models.IntegerField(verbose_name='Динамика количества вакансий по годам для выбранной профессии')),
            ],
        ),
    ]
