#10. Write a Python program to get the file size of a plain file. 
'''def file_read(python):  
        txt = open(python)  
        print(txt.read())  
file_read('python.txt')  '''

def file_size(python):  
        import os  
        statinfo = os.stat(python)  
        return statinfo.st_size  
  
print("File size in bytes of a plain file: ",file_size("python.txt"))  

'''output
[root@test assignment2]# python program10.py
Python Exercises
Java Exercises
Cloud Practice
Basic Learning
Andriod Training
Framework Training'''
