import sys

print(sys.path)

from os.path import abspath, join, dirname

sys.path.insert(0, join(abspath(dirname(__file__)), 'src'))
