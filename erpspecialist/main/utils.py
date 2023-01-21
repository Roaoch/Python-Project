import requests
import re
from typing import List, Dict


__CLEANER = re.compile('<.*?>')


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
            'salary': full_vacancy['salary'],
            'area': full_vacancy['area'],
            'published_at': full_vacancy['published_at']
        })
    return result
