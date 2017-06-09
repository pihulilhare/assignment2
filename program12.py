#12  Write a Python program to copy the contents of a file to another file

from shutil import copyfile

import os

os.system("touch File2.txt ")
copyfile('File1.txt', 'File2.txt')
