"""UserConf - Tests - Settings unit tests."""

from os import remove, rmdir
from os.path import join, exists
import unittest

# We import "paths" to include the "src" directory in "sys.path" so that we can
# import "userconf".
import paths

from userconf import UserConf


class UserConfSettingsTestCase(unittest.TestCase):
    """UserConf settings unit tests."""

    def setUp(self):
        """Initialize each test.

        This method is called before running each test.
        """
        # Initialize the class with a valid application ID
        self.uc = UserConf("userconf_test_app")

    def test_set_get(self):
        """Test the `UserConf.settings.set` and `UserConf.settings.get`
        methods.
        """
        i = "id"
        v = "value"

        self.uc.settings.set(i, v)
        self.assertEqual(self.uc.settings.get(i), v)

    def test_set_get_update(self):
        """Test the `UserConf.settings.set` and `UserConf.settings.get` methods
        when updating a setting."""
        i = "id"

        for v in ("value1", "value2"):
            self.uc.settings.set(i, v)
            self.assertEqual(self.uc.settings.get(i), v)

    def test_get_no_exists(self):
        """Test the `UserConf.settings.get` method when a setting doesn't
        exist.
        """
        self.assertIsNone(self.uc.settings.get("key"))

    def test_get_no_exists_default(self):
        """Test the `UserConf.settings.get` method when a setting doesn't exist
        and there is a default value.
        """
        i = "id"
        v = "value"

        self.assertEqual(self.uc.settings.get(i, v), v)

    def test_contains_true(self):
        """Test the `UserConf.settings.contains` method when the setting
        exists."""
        i = "id"
        v = "value"

        self.uc.settings.set(i, v)
        self.assertTrue(self.uc.settings.contains(i))

    def test_contains_false(self):
        """Test the `UserConf.settings.contains` method when the setting
        doesn't exist.
        """
        self.assertFalse(self.uc.settings.contains("id"))

    def test_get_all(self):
        """Test the `UserConf.settings.get_all` method."""
        s = {"id1": "value1", "id2": "value2"}

        for i, v in s.items():
            self.uc.settings.set(i, v)

        self.assertEqual(self.uc.settings.get_all(), list(s.keys()))

    def test_delete(self):
        """Test the `UserConf.settings.delete` method."""
        i = "id"
        v = "value"

        self.uc.settings.set(i, v)
        self.uc.settings.delete(i)

        self.assertEqual(len(self.uc.settings.get_all()), 0)

    def test_delete_no_exists(self):
        """Test the `UserConf.settings.delete` method when the setting doesn't
        exist.
        """
        self.uc.settings.delete("id")

    def test_delete_all(self):
        """Test the `UserConf.settings.delete_all` method."""
        s = {"id1": "value1", "id2": "value2"}

        for i, v in s.items():
            self.uc.settings.set(i, v)

        self.uc.settings.delete_all()
        self.assertEqual(len(self.uc.settings.get_all()), 0)

    def test_delete_all_empty(self):
        """Test the `UserConf.settings.delete_all` method when there are no
        settings.
        """
        self.uc.settings.delete_all()
        self.assertEqual(len(self.uc.settings.get_all()), 0)

    def tearDown(self):
        """Close each test.

        This method is called after running each test, even if the test method
        raises an exception.
        """
        data_path = self.uc.data_path
        settings_path = join(data_path, "settings.json")

        if exists(settings_path):
            remove(settings_path)

        if exists(data_path):
            rmdir(data_path)


if __name__ == "__main__":
    unittest.main()
