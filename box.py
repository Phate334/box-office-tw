import os
from pathlib import Path

from box_office_tw import DownloadManager

base_path = Path(os.getcwd()).joinpath('docs')

dm = DownloadManager(base_path)
