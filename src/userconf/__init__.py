"""userconf

Application user settings management library.
"""

from typing import Optional, List
import os
import pathlib
import re
import json


__version__ = "0.3.0"

_id_regex = r"[a-zA-Z0-9-_]+$"
_app_id = None

_user_dir = str(pathlib.Path.home())
_app_set_dir = None
_app_set_fname = "settings.json"
_app_set_file = None


def _check_app_id_valid(app_id):
    """Checks if an application ID is valid and raises an Exception if it's
    not.
    """

    if re.match(_id_regex, app_id) is None:
        raise Exception(
            "Invalid application ID. The ID must be either None or a string "
            "containing only letters, numbers, hyphens or underscores."
        )


def _check_set_id_valid(set_id):
    """Checks if a setting ID is valid and raises an Exception if it's not.
    """

    if re.match(_id_regex, set_id) is None:
        raise Exception(
            "Invalid setting ID. The ID must be either None or a string "
            "containing only letters, numbers, hyphens or underscores."
        )


def _check_app_id():
    """Checks if the current working application ID is set and raises an
    Exception if it's not.
    """

    global _app_id

    if _app_id is None:
        raise Exception("Working application ID not set.")


def get_application_id() -> Optional[str]:
    """Returns the working application ID.

    Returns:
        Optional[str]: Working application ID.
    """

    global _app_id
    return _app_id


def set_application_id(app_id: Optional[str]):
    """Sets the working application ID. An Exception is raised if the ID is
    invalid.

    Args:
        app_id (Optional[str]): New working application ID. The ID can be a
            string or None (to delete the current value). If the ID is a
            string, it must contain only letters, numbers, hyphens or
            underscores.
    """

    global _app_id, _user_dir, _app_set_dir, _app_set_file

    if app_id is None:
        _app_set_dir = None
        _app_set_file = None
    else:
        # Check the ID
        _check_app_id_valid(app_id)

        # Update the paths
        _app_set_dir = os.path.join(_user_dir, f".{app_id}")
        _app_set_file = os.path.join(_app_set_dir, _app_set_fname)

    # Update the application ID
    _app_id = app_id


def get_all_setting_ids() -> List[str]:
    """Returns a list with the IDs of all existing settings. An exception is
    raised if the working application ID is not set.

    Returns:
        List[str]: Setting IDs.
    """

    global _app_id
    set_ids = []

    # Check the working application ID
    _check_app_id()

    # Check if the settings file exists
    if os.path.exists(_app_set_file):
        # Read settings
        with open(_app_set_file, "r") as f:
            settings = json.load(f)
            set_ids = list(settings.keys())

    return set_ids


def setting_exists(set_id: str) -> bool:
    """Returns whether a setting exists or not, given its ID. An exception is
    raised if the working application ID is not set or if the setting ID is
    invalid. The setting ID must contain only letters, numbers, hyphens or
    underscores.

    Args:
        set_id (str): Setting ID.

    Returns:
        bool: True if the setting exists or False otherwise.
    """

    global _id_regex, _app_id, _app_set_file
    exists = False

    # Check the working application ID and the setting ID
    _check_app_id()
    _check_set_id_valid(set_id)

    # Check if the settings file exists
    if os.path.exists(_app_set_file):
        # Read settings
        with open(_app_set_file, "r") as f:
            settings = json.load(f)
            exists = set_id in settings

    return exists


def get_setting_value(
    set_id: str, default_value: Optional[object] = None
) -> Optional[object]:
    """Returns the value of a setting given its ID, or a default value if the
    setting doesn't exist. An exception is raised if the working application ID
    is not set or if the setting ID is invalid. The setting ID must contain
    only letters, numbers, hyphens or underscores.

    Args:
        set_id (str): Setting ID.
        default_value (Optional[object]): Value to return if the setting
            doesn't exist. This value must be a JSON serializable object or
            None.

    Returns:
        Optional[object]: Setting value.
    """

    global _id_regex, _app_id, _app_set_file
    value = default_value

    # Check the working application ID and the setting ID
    _check_app_id()
    _check_set_id_valid(set_id)

    # Check if the settings file exists
    if os.path.exists(_app_set_file):
        # Read settings
        with open(_app_set_file, "r") as f:
            settings = json.load(f)

            if set_id in settings:
                value = settings[set_id]

    return value


def set_setting_value(set_id: str, value: Optional[object]):
    """Sets the value of a setting given its ID. An exception is raised if the
    working application ID is not set or if the setting ID is invalid. The
    setting ID must contain only letters, numbers, hyphens or underscores.

    Args:
        set_id (str): Setting ID.
        value (Optional[object]): New setting value. This value must be a JSON
            serializable object or None.
    """

    global _app_id, _app_set_dir, _app_set_file

    # Check the working application ID and the setting ID
    _check_app_id()
    _check_set_id_valid(set_id)

    # If the settings directory doesn't exist, we create it.
    if not os.path.exists(_app_set_dir):
        os.makedirs(_app_set_dir)

    # Check if the settings file exists
    if os.path.exists(_app_set_file):
        # Read settings
        with open(_app_set_file, "r") as f:
            settings = json.load(f)
    else:
        # Default settings
        settings = dict()

    # Update settings
    settings[set_id] = value

    # Write settings
    with open(_app_set_file, "w") as f:
        json.dump(settings, f, indent=4, ensure_ascii=False)


def clear_setting(set_id: str):
    """Deletes a setting given its ID. No exception is raised if the setting
    doesn't exist. An exception is raised if the working application ID is not
    set or if the setting ID is invalid. The setting ID must contain only
    letters, numbers, hyphens or underscores.

    Args:
        set_id (str): Setting ID.
    """

    global _app_id, _app_set_file

    # Check the working application ID and the setting ID
    _check_app_id()
    _check_set_id_valid(set_id)

    # Check if the settings file exists
    if os.path.exists(_app_set_file):
        # Read settings
        with open(_app_set_file, "r") as f:
            settings = json.load(f)

        # Check if the setting exists
        if set_id in settings:
            # Update settings
            del(settings[set_id])

            # Write settings
            with open(_app_set_file, "w") as f:
                json.dump(settings, f, indent=4, ensure_ascii=False)


def clear_all_settings():
    """Deletes the settings directory, including the settings file. An
    exception is raised if the working application ID is not set.
    """

    global _app_id, _app_set_dir, _app_set_file

    # Check the working application ID
    _check_app_id()

    # Before deleting the settings directory with "os.rmdir", we need to delete
    # all its files (which should be only the settings file). Otherwise, an
    # exception would be raised from "os.rmdir".

    # Check if the settings file exists
    if os.path.exists(_app_set_file):
        os.remove(_app_set_file)

    # Check if the settings directory exists
    if os.path.exists(_app_set_dir):
        os.rmdir(_app_set_dir)
