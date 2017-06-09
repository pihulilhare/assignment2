
#12  Write a Python program to copy the contents of a file to another file

from shutil import copyfile

import os

os.system("touch File2.txt ")
copyfile('File1.txt', 'File2.txt')

''' Output
[root@test assignment2]# python program12.py
[root@test assignment2]# cat File1.txt
Andriod
Java
MongoDb
Python
Php
Ruby
[root@test assignment2]# cat File2.txt
Andriod
Java
MongoDb
Python
Php
Ruby'''
