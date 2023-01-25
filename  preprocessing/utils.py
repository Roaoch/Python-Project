import re
from typing import Dict, List


class Utils:
    currency_to_rub = {
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

    @staticmethod
    def clean_skills(skills: str) -> list:
        cleaner = re.compile('<.*?>')
        space_cleaner = re.compile('(\s\s+)|(\xa0)')

        result = re.sub(cleaner, '', skills)
        return re.sub(space_cleaner, ' ', result).strip().split('\n')

    @staticmethod
    def get_salary(salary_from: float, salary_to: float, salary_currency: str) -> float:
        return (salary_from + salary_to) / 2 * Utils.currency_to_rub[salary_currency]

    @staticmethod
    def add_to_or_update(dictionary: Dict[any, any], key: any, value: any) -> None:
        if dictionary.__contains__(key):
            dictionary[key] += value
        else:
            dictionary.update({key: value})

    @staticmethod
    def slice_dict(dictionary: dict, end: int):
        result = {}
        i = 0
        for key, value in dictionary.items():
            i += 1
            if i <= end:
                result.update({key: value})
            else:
                break
        return result

    @staticmethod
    def dict_difference(sliced_dict: Dict[str, float], full_dict: Dict[str, float]) -> Dict[str, float]:
        return {key: full_dict[key] for key in full_dict.keys() if key not in sliced_dict.keys()}

    @staticmethod
    def wrap_text(text: str, separators: List[str]):
        result = text
        for sep in separators:
            if text.__contains__(sep):
                result = "\n".join(text.split(sep, 1))
                break
        return result

    @staticmethod
    def sort_by_value(dictionary: dict):
        return dict(sorted(
            [item for item in dictionary.items()],
            key=lambda e: e[1],
            reverse=True
        ))
