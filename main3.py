#import click
from pathlib import Path
import os

paths = (os.path.join(root, filename)
        for root, dirs, filenames in os.walk('D:\HOMEWORK9\directory')
        for filename in filenames)

for path in paths:
    newname = path.replace('-', '\\')
    if newname != path:
        os.renames(path, newname)