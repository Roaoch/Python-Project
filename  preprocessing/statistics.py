import pandas as pd
from typing import List
from utils import Utils
from datetime import datetime


class Statistics:
    def __init__(self, vacancy_name: List[str], file_name: str):
        self.__vacancy_name = '|'.join(vacancy_name)
        self.__data = pd.read_csv(file_name).dropna()

        self.all_salary_level = {}
        self.all_vacancies_count = {}
        self.salary_level = {}
        self.vacancies_count = {}
        self.by_city_level = {}
        self.vacancies_part = {}
        self.year_skills = {}

        self.__get_statistics()

    def __get_statistics(self):
        self.__data['published_at'] = \
            [datetime.strptime(date, '%Y-%m-%dT%H:%M:%S%z').year for date in self.__data['published_at']]
        self.__data['key_skills'] = [Utils.clean_skills(skills) for skills in self.__data['key_skills']]
        self.__data['salary'] = [Utils.get_salary(value[2], value[3], value[4]) for value in self.__data.values]
        all_count = self.__data.shape[0]

        for year in self.__data['published_at'].unique():
            by_year = self.__data[self.__data['published_at'] == year]
            self.all_salary_level.update({year: by_year['salary'].mean()})
            self.all_vacancies_count.update({year: by_year.shape[0]})

            vac_by_year = by_year[by_year['name'].str.contains(self.__vacancy_name)]
            self.salary_level.update({year: vac_by_year['salary'].mean()})
            self.vacancies_count.update({year: vac_by_year.shape[0]})

            skills = {}
            for x in vac_by_year['key_skills']:
                for y in x:
                    Utils.add_to_or_update(skills, y, 1)
            skills = Utils.sort_by_value(skills)
            self.year_skills.update({year: list(skills.keys())[:10]})

        for city in self.__data['area_name'].unique():
            by_city = self.__data[self.__data['area_name'] == city]
            part = by_city.shape[0] / all_count
            if part >= 0.01:
                self.vacancies_part.update({city: part})
                self.by_city_level.update({city: by_city['salary'].mean()})
        self.by_city_level = Utils.sort_by_value(self.by_city_level)
        self.vacancies_part = Utils.sort_by_value(self.vacancies_part)
