# UserConf
UserConf is a user configuration management Python library. It stores key-value
settings in a JSON file inside the user home directory.

- Version: 0.5.0
- Author: Jose A. Jimenez (jajimenezcarm@gmail.com)
- License: MIT License
- Repository: https://github.com/jajimenez/userconf

## Usage example

```python
from userconf import Userconf

# Create an instance of the Userconf class providing an application ID. The
# settings will be saved in a JSON file named "settings.json" in a directory
# which name is the concatenation of the dot character "." and the application
# ID. This directory will be created inside the user's home directory (e.g.
# "/home/user/example-app").
uc = Userconf("example-app")

# Set a setting value providing the setting ID and the value. The value can be
# any JSON serializable object (a string, an integer, a list, a dictionary...).
uc.set("example-id", "Example value")

# Get a setting value given the setting ID. If the ID doesn't exist, None is
# returned.
v = uc.get("example-id")

# Set a default value to return if the setting ID doesn't exist
v = uc.get("example-id-2", "Default value")

# Delete a setting given its ID
uc.delete("example-id")

# Delete all the settings. The settings JSON file is deleted. The directory
# containing the file is deleted as well as long as it doesn't have other
# files or directories.
uc.delete_all()
```

## Userconf class methods

```python
get_all(self) -> list[str]
contains(self, _id: str) -> bool
get(self, _id: str, default: Optional[Any] = None) -> Optional[Any]
set(self, _id: str, value: Optional[Any])
delete(self, _id: str)
delete_all(self)
```

## How to install

We can install Userconf through PIP:

```bash
pip install userconf
```

Alternatively, we can generate and install the **built package** or the
**source archive** from the source code. The *wheel* package is needed for
generating the built package from the project directory:

To generate and install the **built package** (preferred), run the
following commands:

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
