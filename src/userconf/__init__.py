"""UserConf.

UserConf is a user configuration management Python library. It stores key-value
settings in a JSON file and manages data files and directories. The JSON file
and the data files and directories are inside a directory that is inside the
user home directory.
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
        # Absolute path of the data directory
        self._data_path = None

        # Managers
        self._settings = None
        self._files = None

        # This assigns the manager variables and may raise KeyValidationError
        self.app_id = app_id

    @property
    def app_id(self) -> str:
        """Get the application ID.

        :return: Application ID.
        """
        return self._app_id

    @app_id.setter
    def app_id(self, value: str):
        """Set the application ID.

        A `KeyValidationError` exception is raised if the ID invalid.

        :param app_id: Application ID. The name of the data directory is a
        period (".") followed by the application ID. The data directory is
        inside the user home directory. This ID must contain at least 1
        character and must contain only letters, numbers, hyphens or
        underscores.
        """
        validate_key(value)  # This call may raise KeyValidationError
        self._app_id = value

        # Paths
        user_path = str(Path.home())
        self._data_path = join(user_path, f".{value}")

        settings_path = join(self._data_path, "settings.json")
        files_path = join(self._data_path, "files")

        # Managers
        self._settings = SettingsManager(settings_path)
        self._files = FilesManager(files_path)

    @property
    def data_path(self) -> str:
        """Return the absolute path of the data directory.

        :return: Directory path.
        """
        return self._data_path

    @property
    def settings(self) -> SettingsManager:
        """Get the settings manager.

        :return: `SettingsManager` instance.
        """
        return self._settings

    @property
    def files(self) -> FilesManager:
        """Get the files manager.

        :return: `FilesManager` instance.
        """
        return self._files
