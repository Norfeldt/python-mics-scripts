# coding: utf-8
import os
for (path, subdirs, files) in os.walk(os.getcwd()):
    level = path.replace(os.getcwd(),'').count(os.path.sep)
    indent = ' ' * 4 * level
    print indent, os.path.basename(path)
    
for (path, subdirs, files) in os.walk(os.getcwd()):
    print subdirs
	break
