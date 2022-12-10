"""UserConf - Validation."""

import re


KEY_RE = r"[a-zA-Z0-9-_]+$"  # Setting/file key regular expression


class KeyValidationError(Exception):
    """Exception for application ID or setting/file key validation errors."""

    MESSAGE = (
        "Invalid key. The key must contain at least 1 character and only "
        "letters, numbers, hyphens or underscores."
    )

    def __init__(self, *args):
        """Class initializer."""
        super().__init__(KeyValidationError.MESSAGE, *args)


def validate_key(key: str):
    """Validate an application ID or a setting/file key.

    If `key` is valid, this function does nothing. Otherwise, a
    `KeyValidationError` exception is raised.

    :param key: Application ID or setting/file key.
    """
    if type(key) != str or re.match(KEY_RE, key) is None:
        raise KeyValidationError()
