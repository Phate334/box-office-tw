import os
from pathlib import Path

from box_office_tw import DownloadManager, Converter

base_path = Path(os.getcwd()).joinpath('docs')

dm = DownloadManager(base_path)
dm.fetch()

cov = Converter(base_path)
cov.run()
