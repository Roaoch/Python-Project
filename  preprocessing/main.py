from report import Report
from statistics import Statistics


stat = Statistics([
    'erp',
    'enterprise resource planning',
    'abap',
    'crm',
    'help desk',
    'helpdesk',
    'service desk',
    'servicedesk',
    'bi',
    'sap'
], 'vacancies_with_skills.csv')

report = Report()
report.generate_excel(
    stat.all_salary_level,
    stat.all_vacancies_count,
    stat.salary_level,
    stat.vacancies_count,
    stat.by_city_level,
    stat.vacancies_part,
    stat.year_skills
)
report.generate_image(
    'ERP-специалист',
    stat.all_salary_level,
    stat.all_vacancies_count,
    stat.salary_level,
    stat.vacancies_count,
    stat.by_city_level,
    stat.vacancies_part,
    stat.year_skills
)
