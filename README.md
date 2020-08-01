# UserConf

## Introduction

UserConf is a Python library to manage application user settings. It allows you
to write and read key-value settings for a Python application in a JSON file
inside the home directory of the user who is running the application.

#### Project information

- Version: 0.3.0
- Author: Jose A. Jimenez (jajimenezcarm@gmail.com)
- License: MIT

## Usage example

```python
import userconf as uc

# Set the working application ID. The JSON file containing the settings will be
# saved in a directory which name is the dot character "." followed by the ID
# provided when calling the following function. This directory will be created
# inside the user's home directory.
uc.set_application_id("exampleapp")

# Write a setting value. This is done by providing its ID and value. The value
# can be any JSON serializable object (e.g. a string, a list, a dictionary...).
uc.set_setting_value("setting_example", "Example value")

# Read a setting value. This is done by providing its ID and an optional
# default value that will be returned if the setting doesn't exist.
v = uc.get_setting_value("setting_example", "Default value")
```

## Main functions

```python
get_application_id() -> Optional[str]
set_application_id(app_id: Optional[str])

get_all_setting_ids() -> List[str]
setting_exists(set_id: str) -> bool
get_setting_value(set_id: str, default_value: Optional[object] = None) -> Optional[object]
set_setting_value(set_id: str, value: Optional[object])

clear_setting(set_id: str)
clear_all_settings()
```

## Requirements

#### For installing the library:

- Python >= 3.6

#### For building the library:

- Python >= 3.6
- Python libraries:
  - **wheel**

## How to build redistributable files

To build the **Wheel** package, run:

```
python setup.py bdist_wheel
```

To build the **source** package, run:

```
python setup.py sdist
```

In either case, a new directory called ***dist*** will be generated with the
correspondent package.

## How to install the library

You can install the library from the **source code** by running:

```
python setup.py install
```

Or from the **Wheel** or **source** package with PIP by running:

```
pip install ./dist/<package_file>
```

Where `<package_file>` is the package file name.
