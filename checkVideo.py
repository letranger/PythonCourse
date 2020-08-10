#!/usr/bin/env python3

import filetype
import os
import tempfile
import shutil
import uuid

def IsVideo(fn):
    kind = filetype.guess(fn)
    if kind is None:
        return False, ''
    return True, str(kind.extension)

# Set the directory you want to start from
rootDir = '/Volumes/Vanessa/2020-IPHONE-BACKUP-FILE/'
newRootDir = '/Volumes/Vanessa/Jane/Videos/'
for dirName, subdirList, fileList in os.walk(rootDir):
    for fname in fileList:
        file = os.path.join(dirName, fname)
        #ext = imghdr.what(file)
        kind = filetype.guess(file)
        isV, ext = IsVideo(file)
        if isV:
            if ext not in ('jpg', 'png', 'sqlite'):
                newFile = os.path.join(newRootDir, str(uuid.uuid4())+'.'+ext)
                print(newFile)
                shutil.copy(file, newFile)

        ###if ext == 'jpeg':
        ###    newFile = os.path.join(newRootDir, str(uuid.uuid4())+'.'+ext)
        ###    print(newFile)
        ###    shutil.copy(file, newFile)
