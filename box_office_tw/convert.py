import csv
import codecs
import json
from pathlib import Path


class Converter:
    SOURCE_DIR = 'source'
    JSON_DIR = 'json'
    INDEX_FILE = 'index.json'

    json_pattern = '**/[!index]*.json'
    csv_pattern = '**/*.csv'
    xlsx_pattern = '**/*.xlsx'
    pdf_pattern = '**/*.pdf'

    def __init__(self, base_dir: Path):
        self.source_dir = base_dir.joinpath(self.SOURCE_DIR)
        self.json_dir = base_dir.joinpath(self.JSON_DIR)
        if not self.json_dir.is_dir():
            self.json_dir.mkdir(parents=True, exist_ok=True)
        self.json_index = self.json_dir.joinpath(self.INDEX_FILE)

    def run(self):
        self._from_csv()
        self._from_xlsx()
        self._from_pdf()
        self._build_json_index()

    def _from_csv(self):
        for csv_file in self.source_dir.glob(self.csv_pattern):
            json_file = self._fetch_json_name(csv_file)
            if json_file.is_file():
                continue
            with open(csv_file, 'rb') as f:
                raw = f.read()
                if raw.startswith(codecs.BOM_UTF8):
                    data = raw.decode("utf-8-sig")
                else:
                    data = raw.decode('utf-8')
            data = csv.DictReader([d for d in data.splitlines()],
                                  skipinitialspace=True)
            out = [d for d in data]
            with open(json_file, 'w', encoding='utf-8') as f:
                f.write(json.dumps(out, ensure_ascii=False))

    def _from_xlsx(self):
        pass

    def _from_pdf(self):
        pass

    def _fetch_json_name(self, src: Path) -> Path:
        file_name = src.parts[-1].split('.')[0]
        return self.json_dir.joinpath(file_name + '.json')

    def _build_json_index(self):
        out = [
            j.parts[-1].split('.')[0]
            for j in self.json_dir.glob(self.json_pattern)
        ]
        with open(self.json_index, 'w') as f:
            f.write(json.dumps(out))
