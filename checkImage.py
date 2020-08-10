#!/usr/bin/env python3

import imghdr
import os
import tempfile
import shutil
import uuid

# Set the directory you want to start from
rootDir = '/Volumes/Vanessa/2020-IPHONE-BACKUP-FILE/'
newRootDir = '/Volumes/Vanessa/Jane/'
for dirName, subdirList, fileList in os.walk(rootDir):
    print('Found directory: %s' % dirName)
    for fname in fileList:
        file = os.path.join(dirName, fname)
        ext = imghdr.what(file)
        if ext == 'jpeg':
            newFile = os.path.join(newRootDir, str(uuid.uuid4())+'.'+ext)
            print(newFile)
            shutil.copy(file, newFile)

