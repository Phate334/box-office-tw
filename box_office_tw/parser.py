import re

from requests_html import HTML


def parse_opendata_index(html: HTML):
    with open('opendata.html', 'w', encoding='utf-8') as f:
        f.write(html.html)


def parse_tfi_index(html: HTML):
    for l in html.find('a.file'):
        m = re.search(r"'(.*)'", l.attrs['onclick'])
        # print('https://www.tfi.org.tw' + m.group(1))