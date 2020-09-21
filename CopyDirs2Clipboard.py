# coding: utf-8
import os
import win32clipboard as cb
from time import sleep

cb.OpenClipboard()
root = cb.GetClipboardData()
cb.CloseClipboard()

if os.path.isdir(root):
	os.chdir(root)

	dirs = ""
	for (path, subdirs, files) in os.walk(os.getcwd()):
		dirs = "\n".join(subdirs)
		break
		

	cb.OpenClipboard()
	cb.EmptyClipboard()
	cb.SetClipboardText(dirs)
	cb.CloseClipboard()

	print dirs
	print 
	print "Has been copied to the clipboard"
	
else:
	print "Please copy the root directory to the clipboard and try again"

sleep(4)