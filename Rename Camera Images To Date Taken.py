import exifread
from glob import glob
import os
import win32clipboard as cb

def getDateTaken(imgPath):
	with open(imgPath, 'rb') as img:
		tags = exifread.process_file(img)
		return  str(tags['EXIF DateTimeOriginal']).replace(":",".")

## MAIN CODE ##
dir = r'C:\Users\lanq@nnepharmaplan.com\Pictures\From Windows Phone\Camera Roll'
os.chdir(dir)

for jpg in glob('*jpg'):
	dateTaken = getDateTaken(jpg)
	if str(dateTaken) not in jpg:
		newName = "%s - %s" % (dateTaken, jpg)
		os.rename(jpg, newName)
		print '"'+jpg+'"'+ ' renamed to "' + newName + '"'

raw_input("Complete")