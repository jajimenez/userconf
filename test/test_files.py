"""UserConf - Tests - Files unit tests."""

from os import rmdir
from os.path import join
from pathlib import Path
import unittest

# We import "paths" to include the "src" directory in "sys.path" so that we can
# import "userconf".
import paths

from userconf import UserConf


class UserConfFilesTestCase(unittest.TestCase):
    """UserConf files unit tests."""

    def setUp(self):
        """Initialize each test.

        This method is called before running each test.
        """
        # Initialize the class with a valid application ID
        self.uc = UserConf("userconf_test_app")

    def test_path(self):
        """Test the `UserConf.files.get_path` method."""
        user_path = str(Path.home())
        files_path = join(user_path, ".userconf_test_app", "files")
        test_path = join(files_path, "test")

        self.assertEqual(self.uc.files.get_path("test"), test_path)

    def tearDown(self):
        """Close each test.

        This method is called after running each test, even if the test method
        raises an exception.
        """
        data_path = self.uc.data_path
        files_path = join(data_path, "files")

        rmdir(files_path)
        rmdir(data_path)
