import json
from pathlib import Path
from typing import List, Dict

from requests_html import HTMLSession

from .parser import WeeklyData, OpenDataParser, TfiParser


class DownloadManager:
    OPEN_DATA_URL = 'https://data.gov.tw/dataset/94224'
    TFI_WEEKLY_URL = 'https://www.tfi.org.tw/BoxOfficeBulletin/weekly'
    INDEX_FILE = 'index.json'
    DOWNLOAD_DIR = 'source'
    OPENDATA_DIR = 'opendata'
    TFI_DIR = 'tfi'

    def __init__(self, base_dir: Path):
        self.download_dir = base_dir.joinpath(self.DOWNLOAD_DIR)
        self._mkdir(self.download_dir)
        self.opendata_dir = self.download_dir.joinpath(self.OPENDATA_DIR)
        self.opendata_index = self.opendata_dir.joinpath(self.INDEX_FILE)
        self._mkdir(self.opendata_dir)
        self.tfi_dir = self.download_dir.joinpath(self.TFI_DIR)
        self.tfi_weekly_index = self.tfi_dir.joinpath(self.INDEX_FILE)
        self._mkdir(self.tfi_dir)

        self.session = HTMLSession()

    def fetch(self):
        self._fetch_from_opendata()
        self._fetch_from_tfi()

    def _mkdir(self, path: Path):
        if not path.is_dir():
            path.mkdir(parents=True, exist_ok=True)

    def _fetch_from_opendata(self):
        r = self.session.get(self.OPEN_DATA_URL)
        r.raise_for_status()
        parser = OpenDataParser(r.html)
        remote_index = parser.fetch_index()
        local_index = self._load_index(self.opendata_index)
        for data in remote_index:
            self._update_data(self.opendata_dir, local_index, data)

        self._dump_index(self.opendata_index, remote_index)

    def _fetch_from_tfi(self):
        r = self.session.get(self.TFI_WEEKLY_URL)
        r.raise_for_status()
        parser = TfiParser(r.html)
        remote_index = parser.fetch_index()
        local_index = self._load_index(self.tfi_weekly_index)
        for data in remote_index:
            self._update_data(self.tfi_dir, local_index, data)

        self._dump_index(self.tfi_weekly_index, remote_index)

    def _load_index(self, index_path: Path) -> List[Dict]:
        if index_path.is_file():
            with open(index_path, encoding='utf-8') as f:
                return json.loads(f.read())
        else:
            return []

    def _dump_index(self, local_path: Path, index: List[WeeklyData]):
        out = {}
        for i in index:
            data = out.get(i.get_date(), {})
            data[i.get_file_ext()] = i.url
            out[i.get_date()] = data

        with open(local_path, 'w', encoding='utf-8') as f:
            f.write(json.dumps(out, ensure_ascii=False))

    def _update_data(self, dir_path: Path, index: Dict, data: WeeklyData):
        name = data.get_name()
        local_path = dir_path.joinpath(name)
        # download new file.
        if not local_path.is_file():
            self._download(local_path, data.url)
            return
        # download again, if url change.
        old_url = index.get(data.get_date(), {}).get(data.get_file_ext(), '')
        if old_url != data.url:
            self._download(local_path, data.url)

    def _download(self, local_path: Path, url: str):
        res = self.session.get(url)
        res.raise_for_status()
        with open(local_path, 'wb') as f:
            f.write(res.content)
