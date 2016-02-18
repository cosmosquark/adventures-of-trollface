from distutils.core import setup
import py2exe
import os

excludes = ["pywin", "pywin.debugger"] # there will be more in real life...
options = dict(optimize=2,
           dist_dir="build",
           excludes=excludes,
           packages=["win32api"]) 

Mydata_files = []
for files in os.listdir('C:\\Users\\Ben Thompson\\trollface\\v0.3'):
       f1 = 'C:\\Users\\Ben Thompson\\trollface\\v0.3' + files
       if os.path.isfile(f1): # skip directories
           f2 = 'images', [f1]
           Mydata_files.append(f2)

setup(
    options = {'py2exe': {'bundle_files': 1}},
    windows = [{'script': "game.py"}],
    zipfile = None,
)
