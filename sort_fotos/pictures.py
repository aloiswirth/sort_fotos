# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/00_pictures.ipynb (unless otherwise specified).

__all__ = ['fast_scandir', 'mypath', 'my_Dirs', 'stat_data', 'entry_data', 'df1', 'df2']

# Cell

import os
import pandas as pd
from os.path import isfile, join


# Cell

mypath = r"/media/mycloud/My Pictures"

def fast_scandir(dirname):
    subfolders= [f.path for f in os.scandir(dirname) if f.is_dir()]
    for dirname in list(subfolders):
        subfolders.extend(fast_scandir(dirname))
    return subfolders
my_Dirs = fast_scandir(mypath)

# Cell
stat_data = []
entry_data = []

for dirname in my_Dirs:
    with os.scandir(dirname) as dir_content:
        for entry in dir_content:
            if isfile(join(dirname, entry)):
                info = entry.stat()
                stat_data.append(info)
                entry_data.append([dirname, entry])

# Cell
df1 = pd.DataFrame(entry_data)

# Cell
df2 = pd.DataFrame(stat_data)
df2.rename(columns={ 0 : "st_mode", 1: "st_ino", 2 : "st_dev", 3 : "st_nlink", 4 : "st_uid", 5: "st_gid",}, inplace=True)
df2.rename(columns={ 6 : "st_size", 7 : "st_atime", 8 : "st_mtime", 9 : "st_ctime"}, inplace=True)