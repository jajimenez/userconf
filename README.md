# UserConf
UserConf is a user configuration management Python library. It stores key-value
settings in a JSON file and manages data files and directories. The JSON file
and the data files and directories are inside a directory that is inside the
user home directory.

- Version: 0.5.0
- Author: Jose A. Jimenez (jajimenezcarm@gmail.com)
- License: MIT License
- Repository: https://github.com/jajimenez/userconf

## Usage example

```python
from userconf import UserConf

# Create an instance of the UserConf class providing an application ID. The
# settings JSON file is "settings.json" and the directory for data files and
# directories is "files". The "settings.json" file and the "files" directory
# will be created inside a directory which name is a period (".") followed by
# the application ID, which will be created inside the user's home directory
# (e.g. "/home/user/.app/settings.json" and "/home/user/.app/files" in Linux).
uc = UserConf("example-app")

# Set a setting value providing the setting ID and the value. The value can be
# any JSON serializable object (a string, an integer, a list, a dictionary...).
uc.settings.set("example-key", "Example value")

# Get a setting value given the setting ID. If the ID doesn't exist, None is
# returned.
value = uc.settings.get("example-key")

# Set a default value to return if the setting ID doesn't exist
value = uc.settings.get("example-key-2", "Default value")

# Delete a setting given its ID
uc.settings.delete("example-key")

# Delete all the settings
uc.settings.delete_all()

# Get an absolute path for a data file. This doesn't create the file but it
# creates its directory and all the intermediate directories if they don't
# exist, so that the application using this library can save data in this path
# without having to create its directory.
path = uc.files.get_path("example-file.txt")
```

## How to install

We can install UserConf through PIP:

### Install from PyPI (Python Package Index)

```bash
pip install userconf
```

### Install from the source code

```bash
python setup.py install
```

### Generate a package and install it

We can generate and install the **built package** or the **source archive**
from the source code. The *wheel* package is needed for generating the built
package.

To generate and install the **built package** (preferred), run the following
commands from the project directory:

```bash
pip install wheel
python setup.py bdist_wheel
pip install ./dist/notelist*.whl
```

To generate and install the **source archive**, run the following commands from
the project directory:

```bash
python setup.py sdist
pip install ./dist/notelist*.tar.gz
```

## How to run the unit tests

To run all the unit tests, run the following command from the project
directory:

```bash
python -m unittest discover test
```
