"""Userconf unit tests."""

import unittest

# We import "paths" to include the "src" directory in "sys.path" so that we can
# import "userconf".
import paths

from userconf import Userconf, ValidationError


class UserconfTestCase(unittest.TestCase):
    """Userconf unit tests."""

    def setUp(self):
        """Initialize each test.

        This method is called before running each test.
        """
        # Initialize the class with a valid application ID
        self.uc = Userconf("userconf_test_app")

    def test_app_id(self):
        """Test the `Userconf.app_id` property."""
        i1 = "userconf_test_app"
        i2 = "userconf_test_app_2"

        self.assertEqual(self.uc.app_id, i1)

        self.uc.app_id = i2
        self.assertEqual(self.uc.app_id, i2)

    def test_invalid_app_id(self):
        """Test the `Userconf.app_id` property with an invalid value."""
        i = "userconf#test#app"
        self.assertRaises(ValidationError, Userconf, i)

        def _set_app_id(_id):
            self.uc.app_id = _id

        self.assertRaises(ValidationError, _set_app_id, i)

    def test_set_get(self):
        """Test the `Userconf.set` and `Userconf.get` methods."""
        i = "id"
        v = "value"

        self.uc.set(i, v)
        self.assertEqual(self.uc.get(i), v)

    def test_set_get_update(self):
        """Test the `Userconf.set` and `Userconf.get` methods when updating a
        setting."""
        i = "id"

        for v in ("value1", "value2"):
            self.uc.set(i, v)
            self.assertEqual(self.uc.get(i), v)

    def test_get_no_exists(self):
        """Test the `Userconf.get` method when a setting doesn't exist."""
        self.assertIsNone(self.uc.get("id"))

    def test_get_no_exists_default(self):
        """Test the `Userconf.get` method when a setting doesn't exist and
        there is a default value.
        """
        i = "id"
        v = "value"

        self.assertEqual(self.uc.get(i, v), v)

    def test_contains_true(self):
        """Test the `Userconf.contains` method when the setting exists."""
        i = "id"
        v = "value"

        self.uc.set(i, v)
        self.assertTrue(self.uc.contains(i))

    def test_contains_false(self):
        """Test the `Userconf.contains` method when the setting doesn't exist.
        """
        self.assertFalse(self.uc.contains("id"))

    def test_get_all(self):
        """Test the `Userconf.get_all` method."""
        s = {
            "id1": "value1",
            "id2": "value2"
        }

        for i, v in s.items():
            self.uc.set(i, v)

        self.assertEqual(self.uc.get_all(), list(s.keys()))

    def test_delete(self):
        """Test the `Userconf.delete` method."""
        i = "id"
        v = "value"

        self.uc.set(i, v)
        self.uc.delete(i)

        self.assertEqual(len(self.uc.get_all()), 0)

    def test_delete_no_exists(self):
        """Test the `Userconf.delete` method when the setting doesn't exist."""
        self.uc.delete("id")

    def test_delete_all(self):
        """Test the `Userconf.delete_all` method."""
        s = {
            "id1": "value1",
            "id2": "value2"
        }

        for i, v in s.items():
            self.uc.set(i, v)

        self.uc.delete_all()
        self.assertEqual(len(self.uc.get_all()), 0)

    def test_delete_all_empty(self):
        """Test the `Userconf.delete_all` method when there are no settings."""
        self.uc.delete_all()

    def tearDown(self):
        """Close each test.

        This method is called after running each test, even if the test method
        raises an exception.
        """
        self.uc.delete_all()


if __name__ == "__main__":
    unittest.main()
