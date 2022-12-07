"""Userconf.

Userconf is a Python library to manage the user configuration of applications.
It allows you to write and read key-value settings for a Python application in
a JSON file inside the home directory of the user running the application.
"""

from os import listdir, mkdir, remove, rmdir
from os.path import join, exists
from pathlib import Path
import re
import json
from typing import Any, Optional


__version__ = "0.5.0"


class ValidationError(Exception):
    """Exception raised when a value is invalid."""

    pass


class Userconf():
    """User configuration manager."""

    _id_re = r"[a-zA-Z0-9-_]+$"

    _id_error = (
        "Invalid ID. Its value must contain at least 1 character and only "
        "letters, numbers, hyphens or underscores."
    )

    def __init__(self, app_id: str):
        """Initialize the instance.

        :param app_id: Application ID. Its value must contain at least 1
        character and only letters, numbers, hyphens or underscores.
        """
        self._user_dir = str(Path.home())
        self.app_id = app_id

    def _validate_id(self, _id: str):
        """Validate an application or setting ID.

        A `ValidationError` exception is raised if `_id` is invalid.

        :param _id: Application or setting ID.
        """
        if type(_id) != str or re.match(self._id_re, _id) is None:
            raise ValidationError(self._id_error)

    @property
    def app_id(self) -> str:
        """Get the application ID.

        :returns: Application ID.
        """
        return self._app_id

    @app_id.setter
    def app_id(self, value: str):
        """Set the application ID.

        A `ValidationError` exception is raised if `value` is invalid.

        :param value: Application ID. Its value must contain at least 1
        character and only letters, numbers, hyphens or underscores.
        """
        self._validate_id(value)

        self._app_id = value
        self._app_dir = join(self._user_dir, f".{value}")
        self._app_file = join(self._app_dir, "settings.json")

    def _read_data(self) -> dict:
        """Read settings data.

        :returns: Data.
        """
        data = {}

        if exists(self._app_file):
            with open(self._app_file, "r") as f:
                data = json.load(f)

        return data

    def _write_data(self, data: dict):
        """Write settings data.

        :param data: Data.
        """
        if not exists(self._app_dir):
            mkdir(self._app_dir)

        with open(self._app_file, "w") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def get_all(self) -> list[str]:
        """Get all the existing setting IDs.

        :returns: Setting IDs.
        """
        return list(self._read_data().keys())

    def contains(self, _id: str) -> bool:
        """Return whether the manager contains a setting ID or not.

        A `ValidationError` exception is raised if `_id` is invalid.

        :param _id: Setting ID. Its value must contain at least 1 character and
        only letters, numbers, hyphens or underscores.
        :returns: `True` if the setting exists or `False` otherwise.
        """
        self._validate_id(_id)
        return _id in self._read_data()

    def get(self, _id: str, default: Optional[Any] = None) -> Optional[Any]:
        """Return a setting value or a default value if it doesn't exist.

        A `ValidationError` exception is raised if `_id` is invalid.

        :param _id: Setting ID. Its value must contain at least 1 character and
        only letters, numbers, hyphens or underscores.
        :param default: Value to return if the setting doesn't exist.
        :returns: Setting value if the setting exists or `default` otherwise.
        """
        self._validate_id(_id)
        return self._read_data().get(_id, default)

    def set(self, _id: str, value: Optional[Any]):
        """Set a setting value.

        A `ValidationError` exception is raised if `_id` is invalid.

        :param _id: Setting ID. Its value must contain at least 1 character and
        only letters, numbers, hyphens or underscores.
        :param value: Setting value. Its value must be a JSON serializable
        value.
        """
        self._validate_id(_id)

        data = self._read_data()
        data[_id] = value

        self._write_data(data)

    def delete(self, _id: str):
        """Delete a setting.

        No exception is raised if the setting doesn't exist. A
        `ValidationError` exception is raised if `_id` is invalid.

        :param _id: Setting ID. Its value must contain at least 1 character and
        only letters, numbers, hyphens or underscores.
        """
        self._validate_id(_id)
        data = self._read_data()

        if _id in data:
            data.pop(_id)

        self._write_data(data)

    def delete_all(self):
        """Delete the settings file.

        The directory of the settings file is also deleted if it doesn't
        contain other files or directories.
        """
        if exists(self._app_file):
            remove(self._app_file)

        if exists(self._app_dir) and len(listdir(self._app_dir)) == 0:
            rmdir(self._app_dir)
