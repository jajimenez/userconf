"""UserConf - Tests - Root unit tests."""

import unittest

# We import "paths" to include the "src" directory in "sys.path" so that we can
# import "userconf".
import paths

from userconf import UserConf
from userconf.validation import KeyValidationError


class UserConfRootTestCase(unittest.TestCase):
    """UserConf root unit tests."""

    def setUp(self):
        """Initialize each test.

        This method is called before running each test.
        """
        # Initialize the class with a valid application ID
        self.uc = UserConf("userconf_test_app")

    def test_app_id(self):
        """Test the `UserConf.app_id` property."""
        i1 = "userconf_test_app"
        i2 = "userconf_test_app_2"

        self.assertEqual(self.uc.app_id, i1)

        self.uc.app_id = i2
        self.assertEqual(self.uc.app_id, i2)

    def test_invalid_app_id(self):
        """Test the `UserConf.app_id` property with an invalid value."""
        app_id = "userconf#test#app"

        with self.assertRaises(KeyValidationError):
            UserConf(app_id)

        with self.assertRaises(KeyValidationError):
            self.uc.app_id = app_id


if __name__ == "__main__":
    unittest.main()
