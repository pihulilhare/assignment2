# 14 : Write a Python program to read a random line from a file
import random
l = open("File3.txt").read().splitlines()
print random.choice(l)


'''
output:
[root@test assignment2]# python program14.py
"I'm not mad at all! I'm just differently sane!!"
'''

