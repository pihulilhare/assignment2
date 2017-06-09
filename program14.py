# 14 : Write a Python program to read a random line from a file
import random
l = open("File3.txt").read().splitlines()
print random.choice(l)


'''
output:
[root@demo FileHandlingAssignment]# python program14.py
apple
'''

