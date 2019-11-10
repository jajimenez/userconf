# User Settings
# Jose A. Jimenez (jajimenezcarm@gmail.com)

# To generate the PIP packages, run this command:
#     python3 setup.py sdist bdist_wheel

import setuptools


with open("README.md", "rt") as f:
    long_description = f.read()

setuptools.setup(
    name="usersettings",
    version="0.1.0",
    description="Python library to manage application user settings",
    author="Jose A. Jimenez",
    author_email="jajimenezcarm@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jajimenez/usersettings",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X"
    ],
    python_requires=">=3.6",
    packages=setuptools.find_packages()
)
