"""UserConf - Settings."""

from os import makedirs
from os.path import exists, dirname, exists
import json
from typing import Any

from userconf.validation import validate_key


class SettingsManager():
    """User configuration settings manager."""

    def __init__(self, path: str):
        """Initialize the instance loading the settings data from a JSON file.

        If the settings file doesn't exist initially, it will be created, along
        with all its intermediate directories, the first time a setting is
        added or removed.

        :param path: File path.
        """
        self._path = path
        self._load()

    def _load(self) -> dict:
        """Load the settings data from the JSON file."""
        if exists(self._path):
            with open(self._path) as f:
                self._data = json.load(f)
        else:
            self._data = {}

    def _save(self):
        """Save the settings data to the JSON file.

        The file, the file directory and any intermediate directories are
        created if they don't exist.
        """
        dir_path = dirname(self._path)

        if not exists(dir_path):
            makedirs(dir_path)

        with open(self._path, "w") as f:
            json.dump(self._path, f, indent=4, ensure_ascii=False)

    @property
    def path(self) -> str:
        """Return the JSON file path.

        :return: File path.
        """
        return self._path

    def get_all(self) -> list[str]:
        """Get all the setting keys.

        :return: Keys.
        """
        return list(self._data.keys())

    def contains(self, key: str) -> bool:
        """Return whether a setting key exists.

        A `KeyValidationError` exception is raised if the key is invalid.

        :param key: Setting key. It must contain at least 1 character and must
        contain and only letters, numbers, hyphens or underscores.
        :return: Whether the key exists.
        """
        validate_key(key)  # This may raise KeyValidationError
        return key in self._data

    def get(self, key: str, default: Any = None) -> Any:
        """Return the value of a setting key.

        A `KeyValidationError` exception is raised if the key is invalid. If
        the key doesn't exist, a default value is returned.

        :param key: Setting key. It must contain at least 1 character and must
        contain and only letters, numbers, hyphens or underscores.
        :param default: Value to return if the key doesn't exist.
        :return: Setting value or `default`.
        """
        validate_key(key)
        return self._data.get(key, default)

    def set(self, key: str, value: Any):
        """Set the value of a setting key.

        A `KeyValidationError` exception is raised if the key is invalid.

        :param key: Setting key. It must contain at least 1 character and must
        contain and only letters, numbers, hyphens or underscores.
        :param value: Setting value. It must be serializable to JSON.
        """
        validate_key(key)

        self._data[key] = value
        self._save()

    def delete(self, key: str, error: bool = True):
        """Delete a setting key.

        A `KeyValidationError` exception is raised if the key is invalid. An
        `Exception` exception is raised if the key doesn't exist and `error` is
        `True`.

        :param key: Setting key. It must contain at least 1 character and must
        contain and only letters, numbers, hyphens or underscores.
        :param error: Whether to raise an exception if the key doesn't exist.
        """
        validate_key(key)

        if key in self._data:
            self._data.pop(key)
        elif error:
            raise Exception(f'Key "{key}" does not exist')

        self._save()

    def delete_all(self):
        """Delete all the settings keys."""
        self._data = {}
        self._save()
