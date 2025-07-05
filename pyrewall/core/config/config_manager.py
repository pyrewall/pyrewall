import json
import logging
from datetime import datetime
from filelock import FileLock


from os import path, mkdir, unlink
from shutil import copy2

from .models.config_root import ConfigRoot
from .initial_config import INITIAL_CONFIG

from ..env import PYREWALL_CONFIG_STORAGE_DIR, PYREWALL_PRETTY_CONFIG

class ConfigManager:
    config_root: ConfigRoot
    lock: FileLock
    did_commit = False

    def __init__(self):
        self.lock = FileLock(path.join(PYREWALL_CONFIG_STORAGE_DIR, 'config.lock'))
        self.config_file_path = path.join(PYREWALL_CONFIG_STORAGE_DIR, 'config.json')
        self.temp_config_file_path = path.join(PYREWALL_CONFIG_STORAGE_DIR, 'config.json.tmp')
        if not path.exists(self.config_file_path):
            # Seed initial configuration
            self.config_root = INITIAL_CONFIG.model_copy(deep=True)
            self._write_config_to_file(self.config_file_path)
        else:
            if path.exists(self.temp_config_file_path):
                file_to_load = self.temp_config_file_path
            else:
                file_to_load = self.config_file_path

            with open(file_to_load, 'rt') as config_file:
                self.config_root = ConfigRoot(**json.loads(config_file.read()))

    def __enter__(self):
        self.lock.acquire()
        return self
    
    def __exit__(self, type, value, traceback):
        if type is not None:
            pass # TODO handle errors
        if not self.did_commit:
            self._write_config_to_file(self.temp_config_file_path)
        else:
            if path.exists(self.temp_config_file_path):
                unlink(self.temp_config_file_path)
        self.lock.release()

    def _get_current_config_json(self):
        return self.config_root.model_dump_json(
            indent=(2 if PYREWALL_PRETTY_CONFIG else None)
        )
    
    def _ensure_archive_folder_exists(self):
        archive_folder_path = path.join(PYREWALL_CONFIG_STORAGE_DIR, 'archive')
        if not path.isdir(archive_folder_path):
            mkdir(archive_folder_path)
    
    def _write_config_to_file(self, file: str):
        with open(file, 'wt') as config_file:
            config_file.write(self._get_current_config_json())

    def commit(self):
        old_config_modified_date = datetime.fromtimestamp(path.getmtime(self.config_file_path))
        self._ensure_archive_folder_exists()
        archive_filename = f'config.{old_config_modified_date.strftime('%Y%m%d')}.{old_config_modified_date.strftime('%H%M%S')}.json'
        copy2(self.config_file_path, path.join(PYREWALL_CONFIG_STORAGE_DIR, 'archive', archive_filename))
        self._write_config_to_file(self.config_file_path)
        self.did_commit = True
        