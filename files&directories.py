# Python3.7.3

"""Finding file paths using pathlib & os."""


import os
import glob


# Obtaining the current working directory(cwd).

cwd = os.getcwd()
print(cwd)


from pathlib import Path

cwd = Path()
print(cwd.absolute())


# Reading file sizes & modification timestamp.

from datetime import datetime

for name in os.listdir(cwd):
    path = os.path.join(cwd, name)
    size = os.path.getsize(path)
    mtime = datetime.fromtimestamp(os.path.getmtime(path))
    print(f'{name} {size} bytes, modified {mtime}')


# Using pathlib.

from pathlib import Path

for path in cwd.iterdir():
    stats = path.stat()
    size = stats.st_size
    mtime = datetime.fromtimestamp(stats.st_mtime)
    print(f' {path} {size} bytes, modified {mtime}')

    
 # Finding files that match a wildcard pattern.

py_files = glob.glob('*.py')
py_files = list(cwd.glob('**/*.py'))
py_files = list(cwd.glob('**/*.py'))
print(py_files)
