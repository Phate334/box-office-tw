import re
from json import JSONEncoder
from dataclasses import dataclass
from urllib.parse import urljoin
from typing import Sequence

from requests_html import HTML


@dataclass
class WeeklyData:
    start: tuple
    end: tuple
    url: str

    def get_title(self):
        return '{s[0]}{s[1]}{s[2]}-{e[0]}{e[1]}{e[2]}'.format(s=self.start,
                                                              e=self.end)

    def get_save_name(self):
        return '{}.{}'.format(self.get_title(), self.get_file_ext())

    def get_file_ext(self):
        return self.url.split('.')[-1]

    class DataJSONEncoder(JSONEncoder):
        def default(self, o):
            return {'title': o.get_title(), 'url': o.url}


def parse_opendata_index(html: HTML) -> Sequence[WeeklyData]:
    pass


class TfiParser:
    year_pattern = re.compile(r'(\d*)年')
    day_pattern = re.compile(r'(\d{2})/(\d{2})')
    link_pattern = re.compile(r"'(.*)'")

    def __init__(self, html: HTML):
        self.html = html

    def fetch_index(self) -> Sequence[WeeklyData]:
        table_rows = [
            tr for tr in self.html.find('tr') if 'data-id' in tr.attrs
        ]
        result = []
        for r in table_rows:
            td = r.find('td')
            start, end = self.__fetch_date(td[1].text)
            for a in r.find('a'):
                url = self.__fetch_url(a)
                result.append(WeeklyData(start=start, end=end, url=url))
        return result

    def __fetch_date(self, title: str) -> tuple:
        year = self.year_pattern.findall(title)
        start_day, end_day = self.day_pattern.findall(title)

        return (year[0], start_day[0], start_day[1]), (year[-1], end_day[0],
                                                       end_day[1])

    def __fetch_url(self, a: str) -> str:
        path = self.link_pattern.findall(a.attrs['onclick'])[0]
        return urljoin(a.base_url, path)
