#16 : Write a Python program to remove newline characters from a file

def remove_newlines(NewLine):  
    filelist = open(NewLine).readlines()  
    return [s.rstrip('\n') for s in filelist]    
print(remove_newlines("NewLine.txt"))  

'''Output
Python Training\n
Java Training\n
Framework Training\n

[root@test assignment2]# python program16.py
['Python Exercises', 'Java Exercises', 'Cloud Practice', 'Basic Learning', 'Andriod Training', 'Framework Training']'''
