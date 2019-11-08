# User Settings
# Jose A. Jimenez (jajimenezcarm@gmail.com)

import os
import pathlib
import json
from typing import Optional


_app_id = None

_user_home_dir_path = str(pathlib.Path.home())
_app_settings_dir_path = None
_app_settings_file_name = "settings.json"
_app_settings_file_path = None


def get_application_id() -> Optional[str]:
    """Returns the working application ID.

    Returns:
        Current working application ID, which is either a string or None.
    """

    global _app_id
    return _app_id


def set_application_id(id: Optional[str]):
    """Sets the working application ID. An Exception is raised if the ID is not
    valid.

    Args:
        id: New working application ID. The ID must be an alphanumeric word or
            None.
    """

    global _app_id
    global _user_home_dir_path, _app_settings_dir_path, _app_settings_file_path

    # Check the ID
    if (id is not None and (type(id) != str or id == "" or " " in id or
        "\n" in id or "\t" in id or "\r" in id)): \

        raise Exception(
            "Wrong ID. The ID must be a string containing an alphanumeric "
            "word, or None."
        )

    # Update the ID
    _app_id = id

    # Update the paths
    if id is None:
        _app_settings_dir_path = None
        _app_settings_file_path = None
    else:
        _app_settings_dir_path = os.path.join(_user_home_dir_path, "." + id)

        _app_settings_file_path = os.path.join(_app_settings_dir_path,
                                               _app_settings_file_name)


def get_setting_value(id: str, default_value: Optional[object] = None) \
        -> Optional[object]:
    """Returns the value of a setting given its ID, or a default value if the
    setting doesn't exist. An exception is raised if the working application
    ID is not set.

    Args:
        id: Setting ID.
        default_value: Value to return if the setting doesn't exist. This value
                       can be of any type or None (default).

    Returns:
        Value of the setting, which can be None.
    """

    global _app_id, _app_settings_file_path

    # Check the current working application ID
    if _app_id is None:
        raise Exception("Working application ID not set.")

    # Check the ID
    if (type(id) != str or id == "" or " " in id or "\n" in id or "\t" in id or
            "\r" in id):
        raise Exception(
            "Wrong ID. The ID must be a string containing an alphanumeric "
            "word."
        )

    # Default value
    value = default_value

    # Check if the settings file exists
    if os.path.exists(_app_settings_file_path):
        # Read settings
        with open(_app_settings_file_path, "rt") as f:
            text = f.read()

            if text != "":
                settings = json.loads(text, encoding="utf-8")

                if id in settings:
                    # Get the setting value
                    value = settings[id]

    return value


def set_setting_value(id: str, value: Optional[object]):
    """Sets the value of a setting given its ID. An exception is raised if the
    working application ID is not set.

    Args:
        id: Setting ID.
        value: New setting value. This value must be a JSON serializable
               object or None.
    """

    global _app_id, _app_settings_dir_path, _app_settings_file_path

    # Check the current working application ID
    if _app_id is None:
        raise Exception("Working application ID not set.")

    # Check the ID
    if (type(id) != str or id == "" or " " in id or "\n" in id or "\t" in id or
            "\r" in id):
        raise Exception(
            "Wrong ID. The ID must be a string containing an alphanumeric "
            "word."
        )

    # If the settings directory doesn't exist, we create it.
    if not os.path.exists(_app_settings_dir_path):
        os.makedirs(_app_settings_dir_path)

    settings = None

    # Check if the settings file exists
    if os.path.exists(_app_settings_file_path):
        # Read settings
        with open(_app_settings_file_path, "rt") as f:
            text = f.read()

            if text != "":
                settings = json.loads(text, encoding="utf-8")

    if settings is None:
        # Default settings
        settings = dict()

    # Update settings
    settings[id] = value

    # Write settings
    with open(_app_settings_file_path, "wt") as f:
        json.dump(settings, f, indent=4)


def clear_setting(id: str):
    """Deletes a setting given its ID. No exception is raised if the setting
    doesn't exist. An exception is raised if the working application ID is not
    set.

    Args:
        id: Setting ID.
    """

    global _app_id, _app_settings_file_path

    # Check the current working application ID
    if _app_id is None:
        raise Exception("Working application ID not set.")

    # Check the ID
    if (type(id) != str or id == "" or " " in id or "\n" in id or "\t" in id or
            "\r" in id):
        raise Exception(
            "Wrong ID. The ID must be a string containing an alphanumeric "
            "word."
        )

    # Check if the settings file exists
    if not os.path.exists(_app_settings_file_path):
        return

    settings = None

    # Read settings
    with open(_app_settings_file_path, "rt") as f:
        text = f.read()

        if text != "":
            settings = json.loads(text, encoding="utf-8")

    # Check if the setting exists
    if settings is not None and id in settings:
        # Update settings
        del(settings[id])

        # Write settings
        with open(_app_settings_file_path, "wt") as f:
            json.dump(settings, f, indent=4)


def clear_all_settings():
    """Deletes the settings directory, including the settings file. An
    exception is raised if the working application ID is not set.
    """

    global _app_id, _app_settings_dir_path, _app_settings_file_path

    # Check the current working application ID
    if _app_id is None:
        raise Exception("Working application ID not set.")

    # Before deleting the settings directory with "os.rmdir", we need to delete
    # all its files (which should be only the settings file). Otherwise, an
    # exception would be raised from "os.rmdir".

    # Check if the settings file exists
    if os.path.exists(_app_settings_file_path):
        os.remove(_app_settings_file_path)

    # Check if the settings directory exists
    if os.path.exists(_app_settings_dir_path):
        os.rmdir(_app_settings_dir_path)
