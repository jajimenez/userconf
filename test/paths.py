"""Module to insert the "src" folder in "sys.path".
"""

from os.path import dirname, abspath, realpath, join
import sys

current_dir = dirname(abspath(__file__))
src_path = realpath(join(current_dir, "..", "src"))
sys.path.insert(0, src_path)
