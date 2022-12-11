"""Module to add the "src" directory in "sys.path"."""

import sys
from os.path import dirname, abspath, join


_dir = dirname(abspath(__file__))
src_dir = join(_dir, "..", "src")

sys.path.append(src_dir)
