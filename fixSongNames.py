# coding: utf-8
from glob import glob
def correctName(str):
    str=str[3:]
    str=str.replace('_',' ')
    str=str.replace(
    '-', ' - ')
    return str
for f in glob('*.mp3'):
    print correctName(f)
    
import os
for f in glob('*.mp3'):
    os.rename(f, correctName(f).title().replace('.Mp3','.mp3'))
    
