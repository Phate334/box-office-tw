from pathlib import Path

from requests_html import HTMLSession
from requests import codes

from .parser import *


class DownloadManager:
    OPEN_DATA_URL = 'https://data.gov.tw/dataset/94224'
    TFI_WEEKLY_URL = 'https://www.tfi.org.tw/BoxOfficeBulletin/weekly'
    DOWNLOAD_DIR = 'source'
    OPENDATA_DIR = 'opendata'
    TFI_DIR = 'tfi'

    def __init__(self, base_dir: Path):
        self.download_dir = base_dir.joinpath(self.DOWNLOAD_DIR)
        self._mkdir(self.download_dir)
        self.opendata_dir = self.download_dir.joinpath(self.OPENDATA_DIR)
        self._mkdir(self.opendata_dir)
        self.tfi_dir = self.download_dir.joinpath(self.TFI_DIR)
        self._mkdir(self.tfi_dir)

        self.session = HTMLSession()

    def _mkdir(self, path: Path):
        if not path.is_dir():
            path.mkdir(parents=True, exist_ok=True)

    def fetch(self):
        self._fetch_from_opendata()
        self._fetch_from_tfi()

    def _fetch_from_opendata(self):
        r = self.session.get(self.OPEN_DATA_URL)
        r.raise_for_status()
        parse_opendata_index(r.html)

    def _fetch_from_tfi(self):
        r = self.session.get(self.TFI_WEEKLY_URL)
        r.raise_for_status()
        parse_tfi_index(r.html)
