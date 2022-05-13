import importlib
math = importlib.import_module('math')
print(math.sin(2))
mod = importlib.import_module('urllib.request')
print(mod.urlopen('http://www.python.org'))


b = importlib.import_module('.b', __package__)

