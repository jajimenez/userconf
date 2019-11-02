# User Settings
# Jose A. Jimenez (jajimenezcarm@gmail.com)

import os
import pathlib


_app_id = None

_user_home_dir_path = str(pathlib.Path.home())
_app_settings_dir_path = None
_app_settings_file_name = "settings.json"
_app_settings_file_path = None


def get_application_id() -> str:
    """Returns the working application ID.
    """

    global _app_id
    return _app_id


def set_application_id(id: str):
    """Sets the working application ID. An Exception is raised if the ID is not
    valid.

    Args:
        id: New working application ID. The ID must be an alphanumeric word or
            None.
    """

    global _app_id
    global _user_home_dir_path, _app_settings_dir_path, _app_settings_file_path

    if (id is not None and (type(id) != str or id == "" or " " in id or
        "\n" in id or "\t" in id or "\r" in id)): \

        raise Exception(
            "Wrong ID. The ID must be an alphanumeric word or None."
        )

    _app_id = id

    if id is None:
        _app_settings_dir_path = None
        _app_settings_file_path = None
    else:
        _app_settings_dir_path = os.path.join(_user_home_dir_path, "." + id)

        _app_settings_file_path = os.path.join(_app_settings_dir_path,
                                               _app_settings_file_name)


def get_setting_value(id: str, default_value: str) -> str:
    pass


def set_setting_value(id: str, value: str):
    pass


def clear_setting(id: str):
    pass


def clear_all_settings():
    pass
