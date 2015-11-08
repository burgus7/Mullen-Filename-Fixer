#!/usr/bin/env python3
#
# mullen - Renames files for Ms. Mullen's English Class Standard(tm)
#

import os
import configparser
import shutil
import string

print("Reading mullen_cfg.txt for configuration...")

config = configparser.ConfigParser()
config.read(os.path.expanduser('mullen_cfg.txt'))

Settings = config['Mullen']
oldDocDir = Settings['newDocDir']
newDocDir = Settings['oldDocDir']
lastName = Settings['lastName'].upper()
namePrefix = Settings['namePrefix']
namePrefixNeedsEndSpace = Settings['namePrefixNeedsEndSpace']

if namePrefixNeedsEndSpace == "true":
    namePrefix = namePrefix + " "

print("Files to be converted are in: " + oldDocDir)
print("Files after conversion are in: " + newDocDir)
print("Last name: " + lastName)
print("Preparing to fix files...")

for fileName in os.listdir(oldDocDir):
    if fileName.startswith("~$") and fileName.endswith(".docx"):
        print (oldDocDir + fileName + " is a temp file, deleting.")
        os.remove(oldDocDir + "/" + fileName)

    elif fileName.endswith(".docx") and not fileName.startswith(lastName + "_"):
        newName = fileName.replace(namePrefix, "")
        newName = newName.replace(" ", "_")

        oldName = oldDocDir + "/" + fileName
        newName = newDocDir + "/"  + lastName + "_" + newName

        print(oldName + " -> " + newName)
        shutil.copyfile(oldName, newName)

		
