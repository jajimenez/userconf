# UserConf 0.2.0
# Jose A. Jimenez (jajimenezcarm@gmail.com)

# To generate the PIP packages, run this command:
#     python3 setup.py sdist bdist_wheel

import setuptools


with open("README.md", "rt") as f:
    long_description = f.read()

setuptools.setup(
    name="userconf",
    version="0.2.0",
    description="Python library to manage application user settings",
    author="Jose A. Jimenez",
    author_email="jajimenezcarm@gmail.com",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jajimenez/userconf",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires=">=3.6",
    packages=setuptools.find_packages()
)
