""""userconf" unit tests
"""

import os
import unittest
from datetime import datetime
import paths
import userconf as uc


class NoteTestCase(unittest.TestCase):
    """Unit tests for the "userconf" module.
    """

    def setUp(self):
        """Initializes each test. This method is called before calling each
        test method of this class.
        """

        self.app_val_id = f"userconf_test_{int(datetime.now().timestamp())}"
        self.app_inv_id = "example.id"
        self.set_val_id = "set_id"
        self.set_inv_id = "set.id"

        uc.set_application_id(None)

    def tearDown(self):
        """Closes each test. This method is called after calling each test
        method of this class, even if the test method raises an Exception.
        """

        # Check if the settings file exists
        if uc._app_set_file is not None and os.path.exists(uc._app_set_file):
            os.remove(uc._app_set_file)

        # Check if the settings directory exists
        if uc._app_set_dir is not None and os.path.exists(uc._app_set_dir):
            os.rmdir(uc._app_set_dir)

    def test_ids(self):
        """Tests the "_check_app_id_valid" and "_check_set_id_valid" functions.
        """

        # Valid IDs
        uc._check_app_id_valid(self.app_val_id)
        uc._check_set_id_valid(self.app_val_id)

        # Invalid IDs
        self.assertRaises(Exception, uc._check_app_id_valid, self.app_inv_id)
        self.assertRaises(Exception, uc._check_set_id_valid, self.app_inv_id)

    def test_application_id(self):
        """Tests the "_check_app_id", "get_application_id",
        "set_application_id" functions.
        """

        # Working application ID not set
        self.assertRaises(Exception, uc._check_app_id)
        assert uc.get_application_id() is None

        # Invalid working application ID
        self.assertRaises(Exception, uc.set_application_id, self.app_inv_id)

        # Set working application ID
        uc.set_application_id(self.set_val_id)
        assert uc.get_application_id() == self.set_val_id

    def test_settings(self):
        """Tests the "get_all_setting_ids", "setting_exists",
        "get_setting_value" and "set_setting_value".
        """

        # Working application ID not set
        self.assertRaises(Exception, uc.get_all_setting_ids)
        self.assertRaises(Exception, uc.setting_exists, self.set_val_id)
        self.assertRaises(Exception, uc.get_setting_value, self.set_val_id)
        self.assertRaises(Exception, uc.set_setting_value, self.set_val_id)

        # Set a valid application ID
        uc.set_application_id(self.app_val_id)

        # No settings
        assert uc.get_all_setting_ids() == []

        # Invalid setting ID
        self.assertRaises(Exception, uc.setting_exists, self.set_inv_id)
        self.assertRaises(Exception, uc.get_setting_value, self.set_inv_id)
        self.assertRaises(Exception, uc.set_setting_value, self.set_inv_id)

        # Setting doesn't exist
        def_val = "Default"
        val = "Example"

        assert not uc.setting_exists(self.set_val_id)
        assert uc.get_setting_value(self.set_val_id) is None
        assert uc.get_setting_value(self.set_val_id, def_val) == def_val

        # Add setting
        uc.set_setting_value(self.set_val_id, val)

        assert uc.get_all_setting_ids() == [self.set_val_id]
        assert uc.setting_exists(self.set_val_id)
        assert uc.get_setting_value(self.set_val_id) == val
        assert uc.get_setting_value(self.set_val_id, def_val) == val

    def test_clear_settings(self):
        """Tests the "clear_setting" and "clear_all_settings".
        """

        # Working application ID not set
        self.assertRaises(Exception, uc.clear_setting, self.set_val_id)
        self.assertRaises(Exception, uc.clear_all_settings)

        # Set Working application ID
        uc.set_application_id(self.app_val_id)

        # Invalid setting ID
        self.assertRaises(Exception, uc.clear_setting, self.set_inv_id)
        uc.clear_all_settings()

        # Add setting
        val = "Example"

        uc.set_setting_value(self.set_val_id, val)
        uc.clear_setting(self.set_val_id)
        uc.set_setting_value(self.set_val_id, val)
        uc.clear_all_settings()


if __name__ == "__main__":
    unittest.main()
