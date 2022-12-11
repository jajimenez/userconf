"""UserConf - Files."""

from os import makedirs
from os.path import abspath, exists, join


class FilesManager:
    """User configuration file manager."""

    def __init__(self, root_path: str):
        """Initialize the instance with a file directory path.

        The files or directories managed by this class are inside the root
        directory (`root_path`). If the root directory doesn't exist, it will
        be created along all its intermediate directories the first time the
        `get_path` method is called.

        :param root_path: Relative or absolute path of the root directory. If
        it's a relative path, it's converted to its absolute path.
        """
        self._root_path = abspath(root_path)

    @property
    def root_path(self) -> str:
        """Return the absolute path of the root directory.

        :return: Directory path.
        """
        return self._root_path

    def get_path(self, name: str) -> str:
        """Return the absolute path of a managed file or directory.

        The path returned is the absolute path of the root directory
        (`self._root_path`) followed by the name of the given file or directory
        (`name`). If the root directory doesn't exist, it's created along all
        its intermediate directories.

        :param name: File/directory name.
        :return: File/directory path.
        """
        if not exists(self._root_path):
            makedirs(self._root_path)

        return join(self._root_path, name)
