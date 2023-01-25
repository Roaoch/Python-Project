import requests
import re
from datetime import datetime
from typing import List, Dict


__CLEANER = re.compile('<.*?>')
__CURRENCY_TO_RUB = {
        "AZN": 35.68,
        "BYR": 23.91,
        "EUR": 59.90,
        "GEL": 21.74,
        "KGS": 0.76,
        "KZT": 0.13,
        "RUR": 1,
        "UAH": 1.64,
        "USD": 60.66,
        "UZS": 0.0055,
    }


def get_data(raw_data) -> List[Dict[str, any]]:
    result = []
    for vacancy in raw_data.json()['items']:
        if len(result) == 10:
            break
        full_vacancy = requests.get(f'https://api.hh.ru/vacancies/{vacancy["id"]}').json()
        if len(full_vacancy['key_skills']) == 0:
            continue
        clean_desc = re.sub(__CLEANER, '', full_vacancy['description'])
        result.append({
            'name': full_vacancy['name'],
            'description': clean_desc if len(clean_desc) <= 200 else clean_desc[:200] + '...',
            'key_skills': ", ".join([skill['name'] for skill in full_vacancy['key_skills']]),
            'employer': full_vacancy['employer'],
            'salary': get_salary(full_vacancy['salary']),
            'area': full_vacancy['area'],
            'published_at': get_date(full_vacancy['published_at'])
        })
    return result


def get_salary(salary) -> str:
    raw_salary = \
        (salary["from"] + salary["to"]) / 2 if (salary["from"] and salary["to"]) else (salary["from"] or salary["to"])
    return f'{raw_salary * __CURRENCY_TO_RUB[salary["currency"]]} Руб.'


def get_date(date: str) -> str:
    return datetime.strftime(datetime.strptime(date, '%Y-%m-%dT%H:%M:%S%z'), '%Y-%m-%d')
