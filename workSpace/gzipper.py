import gzip
import shutil
import os
path = input("Enter file path: ")
for i in os.listdir(path):
    if i.endswith('.html'):
        with open(path + i, 'rb') as f_in:
            with gzip.open(path + i + ".gz", 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
pathjs = path + '/static/js/'
for i in os.listdir(pathjs):
    if i.endswith('.js'):
        with open(pathjs + i, 'rb') as f_in:
            with gzip.open(pathjs + i + ".gz", 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
pathcss = path + '/static/css/'
for i in os.listdir(pathcss):
    if i.endswith('.css'):
        with open(pathcss + i, 'rb') as f_in:
            with gzip.open(pathcss + i + ".gz", 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
