#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 08:03:25 2018

@author: osboxes
"""

import os
import time

# 1. the files and directories to be backed up are specified in a list
# example on Windows: source = ['"C:\\My Documents"']
# example on Mac OS X and Linux:
source = ['/home/osboxes/Nextcloud/PhD/SpyderProjects/AByteOfPython/problems/backup/source']
# notice we've to use double quotes inside a string for names with spaces in it
# we could've also used a raw string by writing [r'C:\My Documents']
# 2. the backup must be stored in a main backup directory
# example on Windows: target_dir = 'E:\\Backup'
# example on Mac OS X and Linux:
target_dir = '/home/osboxes/Nextcloud/PhD/SpyderProjects/AByteOfPython/problems/backup/destination'
# remember to change this to which folder you will be using
# 3. the files're backed up into a zip file
# 4. the name of the zip archive is the current date and time
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
# create target directory if its not present
if not os.path.exists(target_dir):
    os.mkdir(target_dir)  # make directory
# 5. we use the zip command to put the files in a zip archive
zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))
# run the backup
print('zip command is:')
print(zip_command)
print('running...')
if os.system(zip_command) == 0:
    print('successful backup to', target)
else:
    print('back failed!')
    