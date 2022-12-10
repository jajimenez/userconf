"""UserConf.

UserConf is a user configuration management Python library. It stores key-value
settings in a JSON file inside the user home directory.
"""

from os.path import join
from pathlib import Path

from userconf.validation import validate_key
from userconf.settings import SettingsManager
from userconf.files import FilesManager


__version__ = "0.5.0"


class UserConf():
    """User configuration manager."""

    def __init__(self, app_id: str):
        """Initialize the instance with an application ID.

        The user configuration is stored in a directory named ".<app_id>"
        inside the user home directory. A `KeyValidationError` exception is
        raised if the ID is invalid.

        :param app_id: Application ID. It must contain at least 1 character and
        must contain and only letters, numbers, hyphens or underscores.
        """
        self._data_dir = None

        # Managers
        self._settings = None
        self._files = None

        self.app_id = app_id  # This may raise KeyValidationError

    @property
    def app_id(self) -> str:
        """Get the application ID.

        :returns: Application ID.
        """
        return self._app_id

    @app_id.setter
    def app_id(self, value: str):
        """Set the application ID.

        A `KeyValidationError` exception is raised if `value` is invalid.

        :param app_id: Application ID. The data is stored in a directory named
        ".<app_id>" inside the user home directory. This ID must contain at
        least 1 character and only letters, numbers, hyphens or underscores.
        """
        validate_key(value)  # This call may raise KeyValidationError
        self._app_id = value

        # Paths
        user_dir = str(Path.home())
        self._data_dir = join(user_dir, f".{value}")

        settings_path = join(self._data_dir, "settings.json")
        files_path = join(self._data_dir, "files.json")

        # Managers
        self._settings = SettingsManager(self, settings_path)
        self._files = FilesManager(self, files_path)

    @property
    def data_dir(self) -> str:
        """Return the data directory.

        :return: Data directory.
        """
        return self._data_dir

    @property
    def settings(self) -> SettingsManager:
        """Get the settings manager.

        :returns: `SettingsManager` instance.
        """
        return self._settings

    @property
    def files(self) -> FilesManager:
        """Get the files manager.

        :returns: `FilesManager` instance.
        """
        return self._files
